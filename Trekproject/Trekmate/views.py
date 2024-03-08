from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, LoginForm, PostForm
from .models import Post

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

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect("mylogin")

    context = {'registerform': form}
    return render(request, 'Trekmate/register.html', context=context)

def mylogin(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect("home")
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
