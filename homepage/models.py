from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    displayname = models.CharField(max_length=80)
