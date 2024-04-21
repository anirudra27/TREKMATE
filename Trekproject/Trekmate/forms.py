from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

# Registration Form
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "phone_number", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already in use.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("The two password fields must match.")
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


# Post Blog Creation Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'short_description', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter short description'}), 
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
    

class DestinationForm(forms.Form):
    season = forms.CharField(max_length=30, required=True)
    duration = forms.CharField(max_length=30, required=True)
    location = forms.CharField(max_length=30, required=True)
    difficulty = forms.CharField(max_length=30, required=True)



class DestinationForm(forms.Form):
    SEASON_CHOICES = (
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Autumn', 'Autumn'),
        ('Winter', 'Winter'),
    )
    
    DIFFICULTY_CHOICES = (
        ('Easy', 'Easy'),
        ('Moderate', 'Moderate'),
        ('Hard', 'Hard'),
    )

    duration = forms.CharField(max_length=100, label='Duration (days)')
    season = forms.ChoiceField(choices=SEASON_CHOICES)
    cost = forms.CharField(max_length=50)
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES, label='Difficulty')

class EditProfileForm(forms.ModelForm):
    password = forms.CharField(label='Current Password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput, required=False)
    confirm_new_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        if password and (not self.instance.check_password(password)):
            raise forms.ValidationError('Incorrect current password.')

        if new_password and new_password != confirm_new_password:
            raise forms.ValidationError('New passwords do not match.')

        return cleaned_data