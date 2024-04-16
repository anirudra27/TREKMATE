from django.contrib import admin
from .models import Post, Itinerary, Product, Order, OrderItem, ShippingAddress
from django.http import HttpResponseRedirect
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  
    search_fields = ['title', 'author__username'] 

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('i_id', 'destination', 'itinerary', 'detail_itinerary', 'season', 'cost', 'location', 'duration', 'map_image')
    search_fields = ['destination', 'season', 'location', 'duration']
    fields = ('i_id', 'destination', 'itinerary', 'detail_itinerary', 'season', 'location', 'cost', 'duration', 'map_image')

#shop
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'product_image', 'quantity', 'size')
    search_fields = ['name', 'price', 'size']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_ordered', 'complete', 'transaction_id')
    search_fields = ['user', 'date_ordered']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added')
    search_fields = ['product', 'date_added']

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'address', 'city', 'date_added')
    search_fields = ['user', 'order']