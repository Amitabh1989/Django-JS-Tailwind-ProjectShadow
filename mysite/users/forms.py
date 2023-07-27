from django.contrib.auth.forms import UserCreationForm
from django.forms import forms, BooleanField, CharField

class CustomUserCreationForm(UserCreationForm):
    print("Rendering user registration form")
    name = CharField(max_length=255, required=True)
    name = BooleanField(label='TC', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your name'
        self.fields['tc'].widget.attrs['placeholder'] = 'TC'

