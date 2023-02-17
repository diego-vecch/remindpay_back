from django.db import models

# Create your models here.
class User(models.Model):
    usernId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    group = models.CharField(max_length=200)

class Group(models.Model):
    group_id =models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=200)
