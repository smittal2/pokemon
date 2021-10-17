from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

class AssignPokemon(APIView):
    """
    Class to assign pokemon to user
    """
    def post(self, request):
        return True


class PokemonAbilities(APIView):
    """
    Class to get pokemon abilities of a pokemon
    """
    def get(self, request):
        return True


class UserPokemons(APIView):
    """
    Class to get pokemons of a particular user with pagination
    """
    def get(self, request):
        return True

