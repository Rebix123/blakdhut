from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User


class UserRegisterForm(UserCreationForm):
    
    full_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, help_text='Required. 8 characters minimum.')
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, help_text ='Required. Enter the same password as above, for verification.')
    referral = forms.CharField(max_length=30, required=False, help_text='Optional. Enter a referral code if you have one.')

    class Meta:
        model = User
        fields = ['full_name', 'email', 'username', 'password1', 'password2', 'referral']

