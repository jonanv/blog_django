from django.contrib import admin

# Imports
from .models import Category, Article

# Imports the names
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_display = ('name', 'created_at')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_filter = ('public', 'user__username', 'categories__name')
    list_display = ('title', 'public', 'user', 'created_at')
    ordering = ('-created_at',)

    # Guarda el usuario de forma automatica
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)