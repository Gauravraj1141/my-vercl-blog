from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=22)
    school = models.CharField(max_length=200)
