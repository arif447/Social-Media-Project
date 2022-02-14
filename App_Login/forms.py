from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from App_Login.models import UserProfile
from django import forms

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Put your email'}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Write your username'}))
    password1 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = UserProfile
        exclude = ['user']
