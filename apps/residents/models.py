from django.db import models
from apps.accounts.models import User
# Create your models here.

class Resident(models.Model):
    user = models.OneToOneField(
                                User, 
                                on_delete=models.SET_NULL,
                                null=True, blank=True,
                                )
    fullname = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname
