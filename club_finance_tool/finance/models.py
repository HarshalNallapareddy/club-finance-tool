from django.db import models
# Create your models here.

class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()

# Add the User model to the models.py file
class User(models.Model):
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_institution = models.BooleanField()
    manager_of = models.ManyToManyField(Club, related_name='managers', blank=True)
    member_of = models.ManyToManyField(Club, related_name='members', blank=True)

def __str__(self):
    return self.name 
