from django import forms
from .models import Tweet
from django.contrib.auth.models import UserCreateForm, User
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreateForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }