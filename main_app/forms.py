from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=250)
        # default is required = True
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=250)
        # default is required = True
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password')



class UserProfileForm(forms.ModelForm):
    home_city = forms.CharField(max_length=100, required=False)
    profile_img = forms.URLField(max_length=1000, required=False)
    class Meta:
        model = Profile
        fields = ["home_city", "image"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["home_city", "image"]