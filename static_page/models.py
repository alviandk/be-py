from django.db import models

from ckeditor.fields import RichTextField


class ContactMessage(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=32)
    message = models.TextField()


class AboutUs(models.Model):
    content = RichTextField()