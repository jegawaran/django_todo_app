from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200,default='')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='userdetailapp/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
