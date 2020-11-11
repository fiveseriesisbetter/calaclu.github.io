import os
import datetime

from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length = 70)
    location = models.CharField(max_length=70)
    date = models.DateField(null = True)
    time = models.CharField(max_length=70)
    description = models.TextField()
    host_committee = models.CharField(max_length = 30)
    event_page = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.date}) \n {self.description}"

    @property
    def passed(self):
        return self.date < datetime.date.today()