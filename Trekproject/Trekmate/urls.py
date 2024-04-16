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
    path('recommend/', views.recommend_destination, name='recommend'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('change_password/', views.change_password, name='change_password'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
