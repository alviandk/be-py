from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=32)
    message = models.TextField()