from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OurSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Podaj maila")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')