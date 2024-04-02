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
    path('itinerary/', views.itinerary, name='itinerary'),
]
