__author__ = 'pavel'
from datetime import datetime
from django import forms
from persons.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, max_length=255)