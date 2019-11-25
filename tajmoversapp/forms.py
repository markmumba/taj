from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Usermails


class ContactForm(forms.ModelForm):

    class Meta:
        model = Usermails
        fields = ['subject','message','from_email']
