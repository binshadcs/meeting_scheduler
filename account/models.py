from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    admin = 1 
    staff = 2
    convenor = 3
    chairman = 4
    director = 5
    Role_choice = (
        (admin,'admin'),
        (staff,'staff'),
        (chairman,'chairman'),
        (director, 'director'),
        (convenor,'convenor'),
    )
    role = models.PositiveSmallIntegerField(choices=Role_choice, blank=True, null=True)
