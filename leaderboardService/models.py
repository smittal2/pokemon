from django.db import models
from datetime import *

class UserLeaderboard(models.Model):
    user = models.IntegerField(db_index=True)
    score = models.IntegerField()

    class Meta:
        db_table = 'user_leaderboard'


class LeaderboardHistory(models.Model):
    user = models.IntegerField(db_index=True)
    fight = models.IntegerField(db_index=True)
    score_earned = models.IntegerField()
    created_on = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'leaderboard_history'