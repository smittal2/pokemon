from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'pokemon'


class PokemonAbilities(models.Model):
    type = models.CharField(max_length=512)
    name = models.CharField(max_length=512)
    function = models.CharField(max_length=512)

    class Meta:
        db_table = 'pokemon_abilities'


class UserPokemon(models.Model):
    user = models.IntegerField(db_index=True)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    pokemon_ablities = models.ManyToManyField(PokemonAbilities)

    class Meta:
        db_table = 'user_pokemon'