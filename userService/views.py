from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

class UserLogin(APIView):
    """
    Class to handle user login
    """
    def post(self, request):
        True


class UserSignup(APIView):
    """
    Class to hanle user signup
    """
    def post(self, request):
        True


class UserProfile(APIView):
    """
    Class to get user profile
    """
    def get(self, request):
        True


class AvailableFighters(APIView):
    """
    Class to get users who are active on platform
    """
    def get(self, request):
        True


class UserSettings(APIView):
    """
    Class to get user profile
    """
    def get(self, request):
        True


