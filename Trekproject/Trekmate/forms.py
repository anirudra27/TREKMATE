from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

from .models import Post

#--Create registeration form

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



#---Authenticate user
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        max_length=50,  
        required=True,
        label=False
    )
    password =forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}),label=False)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content'}),
            'post_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'blogger_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blogger name'}),
        }
        