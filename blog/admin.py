from django.contrib import admin
from .models import Category, Location, Post

admin.site.site_header = 'Блогикум'
admin.site.site_title = 'Блогикум'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'pub_date', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'location')
    search_fields = ('title', 'text')