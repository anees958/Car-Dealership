from distutils.command.upload import upload
from operator import mod
from django.db import models


class Team(models.Model):

    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    designation=models.CharField(max_length=250)
    photo=models.ImageField(upload_to='photos/%y/%m/%d')
    facebook_link=models.URLField(max_length=100)
    twiter_link=models.URLField(max_length=100)
    googleplus_link=models.URLField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)
# Create your models here.

    def __str__(self):

      return self.first_name