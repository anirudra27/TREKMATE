from django.contrib import admin
from .models import Post, Category, Gear, Itinerary

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  
    search_fields = ['title', 'author__username'] 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display these fields in the list view
    search_fields = ['name']  # Add search functionality for name

@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'size', 'price')  # Display these fields in the list view
    list_filter = ('category',)  # Add filter based on category
    search_fields = ('name', 'info')  # Add search functionality for name and info fields

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('destination', 'itinerary', 'detail_itinerary', 'season', 'location', 'duration', 'map_image')
    search_fields = ['destination', 'season', 'location', 'duration']
