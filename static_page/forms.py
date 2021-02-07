from django.forms import ModelForm

from .models import ContactMessage


class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']