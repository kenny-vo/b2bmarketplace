from django import forms
from .models import Listing
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['topic', 'budget', 'location', 'description']

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    vendor = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'vendor', )
