from django import forms
from . models import Account, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ['username', 'email']


class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
