
from django.contrib import admin
from django.urls import include, path
from Trekmate import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Trekmate.urls')),
    path('mylogin/', views.mylogin, name='mylogin'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


