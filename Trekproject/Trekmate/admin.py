from django.contrib import admin
from .models import Contact, Post

# registering model in admin interface
admin.site.register(Contact)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Display these fields in the list view
    search_fields = ['title', 'author__username']  # Add search functionality for title and author's username

admin.site.register(Post, PostAdmin)
