from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class User(AbstractUser):
    followings = models.ManyToManyField(User, symmetrical=False, related_name="followers")
    pass