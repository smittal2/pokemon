from django.urls import path
from .views import UserLogin, UserSignup, UserProfile, UserSettings, AvailableFighters


urlpatterns = [
    path(r'v1/login', UserLogin.as_view()),
    path(r'v1/signup', UserSignup.as_view()),
    path(r'v1/get_user_profile', UserProfile.as_view()),
    path(r'v1/get_available_fighters', AvailableFighters.as_view()),
    path(r'v1/get_user_settings', UserSettings.as_view()),
]