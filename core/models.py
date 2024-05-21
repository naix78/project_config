from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    Avatar = models.ImageField(upload_to="avatars/")