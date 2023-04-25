from datetime import time
from django.db import models

# Create your models here.


class Room(models.Model):

    """model to represent a room table

    Args:
        models (model obj): used to map code to database
    """
    name = models.CharField(max_length=200)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        """represent room object"""
        return f"{self.name}: room {self.room_number} on floor {self.floor_number}"


class Meeting(models.Model):
    """model for meeting table

    Args:
        models (model class)
    """
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(8))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room,on_delete=models.CASCADE,)

    def __str__(self):
        """representation of the object"""
        return f"{self.title} at {self.date} on {self.start_time}"
