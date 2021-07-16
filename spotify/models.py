from django.db import models
from api.models import *

class SpotifyToken(models.Model):
    user         = models.CharField(max_length=50,unique= True)
    created_at   = models.DateTimeField(auto_now_add= True)
    refresh_token= models.CharField(max_length=250)
    access_token = models.CharField(max_length=250)
    expires_in   = models.DateTimeField()
    token_type   = models.CharField(max_length=50)

class Vote(models.Model):
    user         = models.CharField(max_length=50,unique= True)
    created_at   = models.DateTimeField(auto_now_add= True)
    song_id      = models.CharField(max_length=50)
    room         = models.ForeignKey(Room, on_delete=models.CASCADE)
    
