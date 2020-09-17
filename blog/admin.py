from django.contrib import admin

# Imports
from .models import Category, Article

# Imports the names
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields('created_at', 'updated_at')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields('created_at', 'updated_at')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)