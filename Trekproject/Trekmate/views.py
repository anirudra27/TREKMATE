from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Post
from .forms import CustomUserCreationForm
from .models import Itinerary
from .models import Post, Product, Order, OrderItem, ShippingAddress
from django.contrib.auth.forms import  AuthenticationForm
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
import json 
import datetime

def homepage(request):
    return render(request, 'Trekmate/home.html')

def destination(request):
    itineraries = Itinerary.objects.all()
    return render(request, 'Trekmate/destination.html', {'itineraries': itineraries})

def shop(request):
	if request.user.is_authenticated:
		user = request.user
		order, created = Order.objects.get_or_create(user=user, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'Trekmate/shop.html', context)



@login_required
def post_list(request):
    posts = Post.objects.all() 
    return render(request, 'Trekmate/post_list.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
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

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'Trekmate/post_detail.html', {'post': post})


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

def itinerary_detail(request, i_id):
    itinerary = get_object_or_404(Itinerary, i_id=i_id)
    return render(request, 'Trekmate/itinerary_detail.html', {'itinerary': itinerary})

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Trekmate/edit_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('post_list'))
    return render(request, 'delete_post.html', {'post': post})

def cart(request):
    user = request.user
    order, created = Order.objects.get_or_create(user=user, complete=False)
    items = order.orderitem_set.all()
    context = {'items': items, 'order': order}
    return render(request, 'Trekmate/cart.html', context)

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product, Order, OrderItem




def checkout(request):
    user = request.user
    order, created = Order.objects.get_or_create(user=user, complete=False)
    items = order.orderitem_set.all()
    context = {'items': items, 'order': order}
    return render(request, 'Trekmate/checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	user = request.user
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(user=user, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user
        total = float(data['form']['total'])

        # Create or retrieve the order
        order, created = Order.objects.get_or_create(user=user, complete=False)
        order.transaction_id = datetime.datetime.now().timestamp()

        if total == order.get_cart_total:
            order.complete = True
            order.save()

            # Save shipping address if provided
            if 'shipping' in data:
                ShippingAddress.objects.create(
                    user=user,
                    order=order,
                    address=data['shipping']['address'],
                    city=data['shipping']['city'],
                )

            return JsonResponse({'message': 'Payment submitted successfully.'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid total amount.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)