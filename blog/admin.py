from django.contrib import admin
from .models import Post, Comments, Categories


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    empty_value_display = '-'


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'body')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass

