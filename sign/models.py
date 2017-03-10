from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Event(models.Model):
    name=models.CharField(max_length=100)
    limit=models.IntegerField()
    status=models.BooleanField()
    address=models.CharField(max_length=200)
    start_time=models.DateTimeField('event time')
    create_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name