
from django.contrib import admin
from django.urls import include, path
from Trekmate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Trekmate.urls')),
    path('mylogin/', views.mylogin, name='mylogin'),
]
