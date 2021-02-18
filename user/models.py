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


class UserProfile(models.Model):
    user = models.OneToOneField(
            DplUser, 
            on_delete=models.CASCADE, 
            related_name='profile'
    )
    name = models.CharField(max_length=128)
    age_joined = models.PositiveIntegerField(null=True)
    profile_picture = models.ImageField(null=True)
    # interest = models.ManyToManyField()
    # last_degree = models.ForeignKey(DplUser, related_name='profiles')
    city_domicile = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f"{self.user.email}'s profile"


class ProfesionalProfile(models.Model):
    user = models.OneToOneField(
            DplUser, 
            on_delete=models.CASCADE, 
            related_name='profesional_profile'
    )
    position = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    linkedin = models.URLField()
    github = models.URLField()
    

    def __str__(self):
        return f"{self.user.email}'s profile"


class EducationProfile(models.Model):
    user = models.ForeignKey(
            DplUser, 
            on_delete=models.CASCADE, 
            related_name='educations'
    )
    COLLEGE_CHOICES = (
        ('DPM', 'Diploma'),
        ('SJN', 'Sarjana'),
        ('MTR', 'Master'),
        ('DTR', 'Doktor'),
    )

    STATUS_CHOICES = (
        ('WTG', 'WAITING'),
        ('APR', 'Approved'),
    )

    college_level = models.CharField(max_length=8, null=True, choices=COLLEGE_CHOICES)
    field_study = models.CharField(max_length=128, null=True)
    university_name = models.CharField(max_length=128, null=True)
    current_semester = models.PositiveIntegerField(null=True)
    status = models.CharField(
        max_length=8, 
        null=True, 
        choices=STATUS_CHOICES, 
        default='WTG'
    )


    def __str__(self):
        return f"{self.user.profile.name}'s education"