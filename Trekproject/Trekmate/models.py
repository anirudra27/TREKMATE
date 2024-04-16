from django.db import models
from django.contrib.auth.models import User

    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    short_description = models.CharField(max_length=300, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.title


#Itinerary

class Itinerary(models.Model):
    i_id = models.CharField(primary_key=True, max_length=10)
    destination = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    cost = models.CharField(max_length=50, default='')
    itinerary = models.TextField()
    detail_itinerary = models.TextField()
    duration = models.CharField(max_length=100)
    map_image = models.ImageField(upload_to='destination_maps')

    def __str__(self):
        return self.destination

#shop
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    product_image = models.ImageField(upload_to='product_images')
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=100, default='M')

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
        
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for item in orderitems:
            shipping = True  
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address