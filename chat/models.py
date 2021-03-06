from django.db import models
from datetime import datetime


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    admin = models.CharField(max_length=250, default="", editable=False)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    msg = models.CharField(max_length=2000, default="", editable=False)
    user = models.CharField(max_length=250)
    date = models.DateTimeField(default=datetime.now, blank=True)
