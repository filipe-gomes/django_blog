from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    twitter = forms.URLField()

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'email', 'twitter', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    twitter = forms.URLField()

    class Meta:
        model = User
        fields = {'firstname', 'lastname', 'username', 'email', 'twitter'}


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ['image']
