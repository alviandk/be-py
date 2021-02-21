from django.contrib import admin

from .models import AboutUs, ContactMessage

admin.site.register(ContactMessage)
admin.site.register(AboutUs)