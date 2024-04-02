from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.widgets import PasswordInput
from .models import Post
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "phone_number", "password1", "password2")

# Post Blog
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'short_description', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter short description'}), 
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content'}),
        }
    