from django import forms
from .models import User, Profile

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]
            # Default user signup is only username and password 

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["home_city", "country", "profile_img"]
