from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class_scool = models.CharField(max_length=10)
