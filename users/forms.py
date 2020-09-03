from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #required is True by default.

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#On the template, the UserUpdateForm and the ProfileUpdateForm will look like a single form. 
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() #required is True by default.

    class Meta:
        model = User
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']