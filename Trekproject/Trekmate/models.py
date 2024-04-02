from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    short_description = models.CharField(max_length=300, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
#E-shop
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Gear(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    size = models.CharField(max_length=50)
    info = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

#Itinerary

class Itinerary(models.Model):
    destination = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    itinerary = models.TextField()
    detail_itinerary = models.TextField()
    duration = models.CharField(max_length=100)
    map_image = models.ImageField(upload_to='destination_maps')

    def __str__(self):
        return self.destination

    