from django.contrib import admin
from .models import Blog, SubCategory, Category, Author;

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


