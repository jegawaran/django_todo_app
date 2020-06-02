from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    firstname = models.CharField(max_length=200,blank=False)
    lastname = models.CharField(max_length=200,blank=False)
    phoneno = models.IntegerField(max_length=15,blank=False)
    emailid = models.EmailField(max_length=80,blank=False)
    address = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now())
    

    def __str__(self):
        return self.firstname
