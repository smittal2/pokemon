from django.test import TestCase
from fightService.models import PokemonFight
from userService.models import User, Session
from pokemonService.models import UserPokemon, Pokemon

class FightRequestTestCase(TestCase):
    def setUp(self):

        user1 = User.objects.create(username="shubham", email='shubham@pokemon.com')
        user2 = User.objects.create(username="kartik", email='kartik@pokemon.com')
        pokemon1 = Pokemon.objects.create(name='Pikachu')
        pokemon2 = Pokemon.objects.create(name='Eevee')
        # UserPokemon.objects.create()
        Session.objects.create(user=user1, current_status='active')
        Session.objects.create(user=user2, current_status='active')

    def check_fight_creation(self):
        """
        Write your test cases here
        """

        # Case - 1
        """
        When request do not contain all the required params
        Bad request should be returned
        """

        # Case 2
        """
        When user is not logged in then 401 should be returned
        """

        # Case 3
        """
        User should not be able to challenge himself
        """

        # Case 4
        """
        The challenged user should be active on platform
        """

        # Case 5
        """
        Pokemons specified in the request should belong to the corresponding users
        """

        # Case 6
        """
        Pokemons for both users should have non zero health
        """

        # Case 7
        """
        Each user should be engaged in one fight at a time, no other request will be created if either of user is in other fight
        """




class RespondFightRequestTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="shubham", email='shubham@pokemon.com')
        user2 = User.objects.create(username="kartik", email='kartik@pokemon.com')
        pokemon1 = Pokemon.objects.create(name='Pikachu')
        pokemon2 = Pokemon.objects.create(name='Eevee')
        # UserPokemon.objects.create()
        Session.objects.create(user=user1, current_status='active')
        Session.objects.create(user=user2, current_status='active')

    def check_fight_creation(self):
        """
        Write your test cases here
        """

        # Case - 1
        """
        User should be logged in
        """

        # Case 2
        """
        Fight id should be valid
        """

        # Case 3
        """
        Fight id should correspond to logged in user only
        """

        # Case 4
        """
        Fight should not be timed out and only in pending state
        """

        # Case 5
        """
        If fight challenger somehow become inactive while other person accepts request then fight should not begin
        """