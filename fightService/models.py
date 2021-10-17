from django.db import models
from datetime import datetime

FIGHT_STATUS_CHOICES = (('pending', 'pending'), ('rejected', 'rejected'), ('accepted', 'accepted'), ('timeout', 'timeout'),
                        ('in_progress', 'in_progress'), ('completed', 'completed'))
"""
pending - A user has challeneged other user and request is not responded by other user
rejected - Other user rejected the fight request
timeout - Request is timed out
accepted - Fight requested is accepted
in_progress - Fight is currently in progress
completed - Fight is completed 
"""

class PokemonFight(models.Model):
    challenger_user_id = models.IntegerField(db_index=True)
    challenger_pokemon_id = models.IntegerField(db_index=True)
    challenged_user_id = models.IntegerField(db_index=True)
    challenged_pokemon_id = models.IntegerField(db_index=True)
    challenged_on = models.DateTimeField(default=datetime.now)
    winner_id = models.IntegerField(db_index=True, null=True)
    status = models.CharField(choices=FIGHT_STATUS_CHOICES, default=FIGHT_STATUS_CHOICES[0][0], max_length=128)

    class Meta:
        db_table = 'pokemon_fight'