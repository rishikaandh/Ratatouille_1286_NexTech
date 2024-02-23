# Enhancer/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField(required=False)
    INTEREST_CHOICES = [
        ('football', 'Football'),
        ('cricket', 'Cricket'),
        ('music', 'Music'),
        ('dance', 'Dance'),
    ]
    interest = forms.MultipleChoiceField(choices=INTEREST_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age', 'interest', 'password1', 'password2']
