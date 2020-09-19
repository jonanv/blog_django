from django.contrib import admin

# Imports
from .models import Page

# Configuracion extra para el panel
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)

# Configuracion de titulos del panel
title = 'Proyecto con Django'
subtitle = 'Panel de gestión'

admin.site.site_title = title # Pestania del nevegador
admin.site.site_header = title
admin.site.index_title = subtitle

# Register your models here.
# Registrar modelo en el panel
admin.site.register(Page, PageAdmin)