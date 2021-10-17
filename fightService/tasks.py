from django.core.exceptions import ObjectDoesNotExist

from fightService.models import PokemonFight


def send_fight_request_to_challenged_user(fight_id):
    try:
        fight_obj = PokemonFight.objects.get(id=fight_id)
    except ObjectDoesNotExist:
        return

    # Send fight request notification to other user through socket


def send_fight_response_to_challenger_user(fight_id):
    try:
        fight_obj = PokemonFight.objects.get(id=fight_id)
    except ObjectDoesNotExist:
        return

    # Send fight response notification to challenger user through socket