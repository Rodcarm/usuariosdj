from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

class User(AbstractBaseUser,PermissionsMixin):

    GENDER_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otros'),
    )

    username = models.CharField(max_length=10,unique=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender =  models.CharField(max_length=1,choices=GENDER_CHOICES, blank=True)
    
    USERNAME_FIELD = 'username'

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.name +' '+self.last_name