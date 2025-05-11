from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class TweetForm(forms.ModelForm):
#     class Meta:
#         model = Tweet
#         fields = ['text', 'photo']

# class UserRegistrationForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-input'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-input'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-input'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'form-input'}))
#     class Meta:
#       model = User
#       fields = ['username', 'email', 'password1', 'password2']

     

from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Tweet form
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

# User registration form
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control rounded-pill p-3 bg-transparent text-light border-light'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control rounded-pill p-3 bg-transparent text-light border-light'
        })
    )
    
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control rounded-pill p-3 bg-transparent text-light border-light'
        })
    )
    
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control rounded-pill p-3 bg-transparent text-light border-light'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
