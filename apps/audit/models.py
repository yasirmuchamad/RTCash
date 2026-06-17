from django.db import models

# Create your models here.
from apps.accounts.models import User

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    object_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)