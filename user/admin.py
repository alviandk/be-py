from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import DplUser, EducationProfile, ProfesionalProfile, UserProfile
from testimonial.models import MemberStory


class UserProfileInline(admin.StackedInline):
    model = UserProfile

class ProfesionalProfileInline(admin.StackedInline):
    model = ProfesionalProfile

class MemberStoryInline(admin.StackedInline):
    max_num = 1
    model = MemberStory


class EducationProfileInline(admin.StackedInline):
    max_num = 1
    model = EducationProfile


class CustomUserAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [UserProfileInline, ProfesionalProfileInline, EducationProfileInline]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = DplUser
    list_display = ('email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(DplUser, CustomUserAdmin)
