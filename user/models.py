from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  is_user = models.BooleanField(default=False)
  is_bank = models.BooleanField(default=False)
  is_moneylender = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)
  first_name = models.CharField(max_length=100, null=False)
  last_name = models.CharField(max_length=100, null=False)


class Bank(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE) 
  name = models.CharField(max_length=100, null=False)
  address = models.CharField(max_length=100, null=False)
  email = models.CharField(max_length=100, null=False)
  interest_rate = models.FloatField(null=False)
  password = models.CharField(max_length=100, null=False)


class Moneylender(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, null=False)
  address = models.CharField(max_length=100, null=False)
  email = models.CharField(max_length=100, null=False)
  interest_rate = models.FloatField(null=False)
  password = models.CharField(max_length=100, null=False)


# Create your models here.
