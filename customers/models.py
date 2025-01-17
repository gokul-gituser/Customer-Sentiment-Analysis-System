from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    pass
   

    def __str__(self):
        return self.username
