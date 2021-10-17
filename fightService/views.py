
import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from userService.decorator import login_required, required_fields
from userService.helpers import check_user_logged_in
from .models import PokemonFight, FIGHT_STATUS_CHOICES
from .tasks import send_fight_request_to_challenged_user, send_fight_response_to_challenger_user
from rest_framework.views import APIView
# Create your views here.

class FightRequest(APIView):

    @login_required
    @required_fields('challenger_pokemon_id', 'challenged_user_id', 'challenged_pokemon_id')
    def post(self, request):
        # Extract required params
        _ = self.get_params(request)

        # Do not proceed if the user is not active on the app
        challenged_user_logged_in_status = check_user_logged_in(self.challenged_user_id)
        if not challenged_user_logged_in_status:
            return HttpResponse(json.dumps(dict(message='User is no longer available to fight')))


        obj = PokemonFight.objects.create(challenger_user_id=self.user.id, challenger_pokemon_id=self.challenger_pokemon_id,
                                          challenged_user_id=self.challenged_user_id, challenged_pokemon_id=self.challenged_pokemon_id)

        # Send notification to other user for fight challenge
        send_fight_request_to_challenged_user.delay(self.fight_id)
        return HttpResponse(json.dumps(dict(status=1, data=dict(fight_id=obj.id))))

    def get_params(self, request):
        self.challenger_pokemon_id = request.POST['challenger_pokemon_id']
        self.challenged_user_id = request.POST['challenged_user_id']
        self.challenged_pokemon_id = request.POST['challenged_pokemon_id']
        self.user = request.user
        return


class RespondFightRequest(APIView):

    @login_required
    @required_fields('fight_id', 'fight_accepted')
    def post(self, request):
        # Extract required params
        _ = self.get_params(request)

        # Check if params are valid or not
        params_validity = self.check_params_validity()
        if type(params_validity) != type(True):
            return params_validity

        # Update the fight status obj
        self.update_fight_obj()

        # Notify challenger user for response from other user
        send_fight_response_to_challenger_user.delay(self.fight_id)
        return HttpResponse(json.dumps(dict(status=1)))

    def get_params(self, request):
        self.fight_id = request.POST['fight_id']
        self.fight_accepted = request.POST['fight_accepted'].lower() == 'true'
        return

    def check_params_validity(self):
        try:
            self.fight_obj = PokemonFight.objects.get(id=self.fight_id)
        except ObjectDoesNotExist:
            return HttpResponseBadRequest(json.dumps(dict(message='Invalid fight')))

        if self.fight_obj.status != FIGHT_STATUS_CHOICES[0][0]:
            return HttpResponseBadRequest(json.dumps(dict(message='Fight response already recorded')))

        return True

    def update_fight_obj(self):
        status = FIGHT_STATUS_CHOICES[2][0] if self.fight_accepted else FIGHT_STATUS_CHOICES[1][0]
        self.fight_obj.status = status
        self.fight_obj.save()
        return