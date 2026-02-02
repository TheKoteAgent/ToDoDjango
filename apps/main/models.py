from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)