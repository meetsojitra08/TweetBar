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

     

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    # Customizing the username field with additional attributes
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control rounded-pill p-3 bg-transparent text-light border-light'
        })
    )
    
    # Customizing the email field with additional attributes
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control rounded-pill p-3 bg-transparent text-light border-light'
        })
    )
    
    # Customizing password1 field with additional attributes
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control rounded-pill p-3 bg-transparent text-light border-light'
        })
    )
    
    # Customizing password2 field (confirm password) with additional attributes
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control rounded-pill p-3 bg-transparent text-light border-light'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']