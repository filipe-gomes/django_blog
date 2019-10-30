from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    twitter = forms.URLField(max_length=100, required=False)
    email = forms.EmailField(max_length=254, required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'twitter', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    twitter = forms.URLField(max_length=100, required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'twitter', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ['image']
