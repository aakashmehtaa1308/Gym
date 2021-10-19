from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'E-mail'}

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['height','weight','category','goal']
        labels={'height':'Height(in cm)','weight':'Weight(in kg)','category':'Category','goal':'Goal'}