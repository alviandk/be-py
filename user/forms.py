from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm


from .models import DplUser, EducationProfile, UserProfile


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = DplUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = DplUser
        fields = ('email',)


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'city_domicile',)
        labels = {
            'name': 'Nama Kamu',
            'city_domicile': 'Domisili Kota'
        }


class EducationProfileForm(ModelForm):
    class Meta:
        model = EducationProfile
        fields = ('university_name', 'field_study', 'college_level', 'current_semester')
        labels = {
            'field_study': 'Jurusan Kuliah',
            'university_name': 'Kuliah di Universitas',
            'current_semester': 'Saat ini Semester',
            'college_level': 'Jenjang Kuliah'
        }
