from django import forms
from .models import Listing
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ListingForm(forms.ModelForm):
    """Listing forms"""

    date_required = forms.DateField(
        widget=forms.DateInput(format=('%m/%d/%Y'),
                               attrs={'class':'myDateClass',
                                      'placeholder':'mm/dd/yyyy'}))


    class Meta:
        model = Listing
        fields = ['topic', 'budget', 'location', 'description', 'requirement1', 'requirement2', 'requirement3', 'date_required']

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Username or Password incorrect.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    vendor = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'vendor', )
