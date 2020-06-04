from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Consumerprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    phoneno = models.CharField(max_length=200,blank=True)
    address = models.TextField(max_length=200,blank=True)
    occupation = models.CharField(max_length=200,blank=True)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='consumer/images/',default="")
    created_date = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.user.username
