from django.urls import path
from .views import PokemonAbilities, UserPokemons, AssignPokemon


urlpatterns = [
    path(r'v1/assign_pokemon', AssignPokemon.as_view()),
    path(r'v1/get_pokemon_abilities', PokemonAbilities.as_view()),
    path(r'v1/get_user_pokemons', UserPokemons.as_view()),
]