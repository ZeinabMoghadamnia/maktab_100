from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomeUser(AbstractUser):
    birth_date = models.DateTimeField(null=True, blank=True)
    