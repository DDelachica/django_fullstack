from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
