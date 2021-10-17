from django.db import models
from datetime import *

STATUS_CHOICES = (('active', 'active'), ('inactive', 'inactive'), ('uninstalled', 'uninstalled'))
"""
active - User currently using the app for this session
inactive - User currently not using the app for this session
uninstalled - User uninstalled the app for this session
"""

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    locality = models.CharField(max_length=128)

    class Meta:
        db_table = 'user'


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=512, unique=True)
    device_info = models.CharField(max_length=512)
    last_logged_in = models.DateTimeField(null=True, default=datetime.now)
    current_status = models.CharField(choices=STATUS_CHOICES, max_length=128)

    class Meta:
        db_table = 'session'


class Settings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sound = models.BooleanField(default=True)
    status = models.CharField(max_length=512)
    other_settings = models.CharField(max_length=512)

    class Meta:
        db_table = 'settings'