from django import forms
from .models import MailStore


class MailStoreForm(forms.ModelForm):
    class Meta:
        model = MailStore
        fields = '__all__'
