from django.urls import path
from .views import FightRequest, RespondFightRequest


urlpatterns = [
    path(r'v1/fight_request', FightRequest.as_view()),
    path(r'v1/respond_fight_request', RespondFightRequest.as_view()),
]