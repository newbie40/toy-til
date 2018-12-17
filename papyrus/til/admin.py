from django.contrib import admin

# Register your models here.
from .models import Category, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'user', 'category']
    list_display = ('title', 'content', 'user', 'category')


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post', {'fields': ['post']}),
        ('Comment', {'fields': ['content']}),
    ]
    list_display = ('content', 'user')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
