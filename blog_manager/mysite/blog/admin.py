from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
# register the model to be displayed in Django Admin Panel
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Comment)
# register comment model for display on Django Admin panel
class CommentAdmin(admin.ModelAdmin):
    # fields that will appear when you create a new object of this class
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']