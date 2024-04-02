from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Post
from .forms import CustomUserCreationForm
from .models import Itinerary

from django.contrib.auth.forms import  AuthenticationForm
from .forms import PostForm

def homepage(request):
    return render(request, 'Trekmate/home.html')

@login_required
def destination(request):
    return render(request, 'Trekmate/destination.html')

@login_required
def shop(request):
    return render(request, 'Trekmate/shop.html')

@login_required
def post_list(request):
    posts = Post.objects.all() 
    return render(request, 'Trekmate/post_list.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been created successfully.')
            return redirect('post_list')
        else:
            messages.error(request, 'Failed to create the post. Please check the form data.')
    else:
        form = PostForm()
    return render(request, 'Trekmate/create_post.html', {'form': form})

from .forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}. Please log in.')
            return redirect("mylogin")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Trekmate/register.html', {'form': form})



def mylogin(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect("home")
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')

    context = {'loginform': form}
    return render(request, 'Trekmate/mylogin.html', context=context)



def user_logout(request):
    logout(request)
    return redirect("home")

@login_required
def dashboard(request):
    return render(request, 'Trekmate/dashboard.html')

def itinerary(request):
    itineraries = Itinerary.objects.all()  
    return render(request, 'Trekmate/itinerary.html', {'itineraries': itineraries})