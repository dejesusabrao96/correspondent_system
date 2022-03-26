from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	is_secretary = models.BooleanField(default=False)
	is_director = models.BooleanField(default=False)
	is_administrator = models.BooleanField(default=False)
	is_vogal = models.BooleanField(default=False)
	is_prezidente = models.BooleanField(default=False)
