from django.utils import timezone
from django.db import models

from datetime import time


RESERVATION_TIME = [
    (time(hour=14, minute=0),  '14:00:00'),
    (time(hour=14, minute=30), '14:30:00'),
    (time(hour=15, minute=0),  '15:00:00'),
    (time(hour=15, minute=30), '15:30:00'),
    (time(hour=16, minute=0),  '16:00:00'),
    (time(hour=16, minute=30), '16:30:00'),
    (time(hour=17, minute=0),  '17:00:00'),
    (time(hour=17, minute=30), '17:30:00'),
    (time(hour=18, minute=0),  '18:00:00'),
    (time(hour=18, minute=30), '18:30:00'),
    (time(hour=19, minute=0),  '19:00:00'),
    (time(hour=19, minute=30), '19:30:00'),
    (time(hour=20, minute=0),  '20:00:00'),
    (time(hour=20, minute=30), '20:30:00'),
    (time(hour=21, minute=0),  '21:00:00'),
    (time(hour=21, minute=30), '21:30:00'),
    (time(hour=22, minute=0),  '22:00:00'),
    (time(hour=22, minute=30), '22:30:00'),
]


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField(default=timezone.now)
    reservation_time = models.TimeField(choices=RESERVATION_TIME, default=time(hour=22, minute=30))
    reservation_slot = models.SmallIntegerField(default=10)

    class Meta:
        unique_together = ['reservation_date', 'reservation_time', 'reservation_slot']

    def __str__(self): 
        return self.first_name


class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name