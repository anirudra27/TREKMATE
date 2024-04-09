from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.mylogin, name="mylogin"),
    path('logout/', views.user_logout, name="user-logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('post_list/', views.post_list, name='post_list'),
    path('create_post/', views.create_post, name='create_post'), 
    path('destination/', views.destination, name='destination'),
    path('shop/', views.shop, name='shop'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('itinerary/<str:i_id>/', views.itinerary_detail, name='itinerary_detail'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('shop/', views.shop, name='shop'),
    
    # path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
