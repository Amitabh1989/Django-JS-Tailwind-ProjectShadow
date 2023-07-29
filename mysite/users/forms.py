from django.contrib.auth.forms import UserCreationForm
from django.forms import forms, BooleanField, CharField
from .models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    print("Rendering user registration form")
    name = CharField(max_length=255, required=True)
    # name = BooleanField(label='TC', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your name'
        self.fields['tc'].widget.attrs['placeholder'] = 'TC'

class UserForm(forms.ModelForm):
    print("User registration form called")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), label='Confirm Password')
    class Meta:
        model = User
        fields = ['name', 'email', 'tc', 'password', "password2"]
        labels = {
            "name": "Enter your name",
            "email": "Enter your official email",
            "tc": "I dont know what is this for!",
            "password": "Enter a 8 characters alpha numberic password",
            "password2": "Re-Enter a 8 characters alpha numberic password",
        }

    