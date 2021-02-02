from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class DplUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class UserProfile(models.Model):
#     user = models.OneToOneField(DplUser, related_name='profile')
#     name = models.CharField(max_length=128)
#     age_joined = models.PositiveIntegerField()
#     interest = models.ManyToManyField()
#     last_degree = models.ForeignKey(DplUser, related_name='profiles')
#     city_domicile = models.ForeignKey(DplUser, related_name='profiles')

#     def __str__(self):
#         return f"{self.user.email}'s profile"
