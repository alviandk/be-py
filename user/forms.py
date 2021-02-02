from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import DplUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = DplUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = DplUser
        fields = ('email',)