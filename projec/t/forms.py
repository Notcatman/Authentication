from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import MinLengthValidator

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(label="Username", max_length=30, min_length=4, validators=[MinLengthValidator(4, message="Username must be at least 4 characters yo")])

    class Meta:
        model = User
        fields = ["username", "email"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(min_length=4, max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
        }),
        error_messages={'min_length': "Username must be at least 4 characters."}
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))