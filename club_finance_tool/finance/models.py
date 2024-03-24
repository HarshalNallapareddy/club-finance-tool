from django.db import models

# Create your models here.
from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100)
    # executives = models.ManyToManyField('User', related_name='executives', blank=True)
    members = models.ManyToManyField('User', related_name='members', blank=True)

class User(models.Model):
    name = models.CharField(max_length=100)
    clubs = models.ManyToManyField(Club)

    def __str__(self):
        return self.name 
