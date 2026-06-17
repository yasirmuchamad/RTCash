from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('ketua', 'Ketua RT'),
        ('bendahara', 'Bendahara'),
        ('warga', 'Warga'),
    )
    role = models.CharField(max_length=20, 
                            choices=ROLE_CHOICES,
                            default='warga'
                            )

    phone_number = models.CharField(max_length=20, blank=True, null=True)
    