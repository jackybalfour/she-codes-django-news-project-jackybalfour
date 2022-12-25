from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class EditUserProfileForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Valid email address required.')

    class Meta:
        model = CustomUser
        fields = ['username','email']