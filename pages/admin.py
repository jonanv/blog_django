from django.contrib import admin

# Imports
from .models import Page

# Configuracion de titulos del panel
title = 'Proyecto con Django'
subtitle = 'Panel de gestión'

admin.site.site_title = title # Pestania del nevegador
admin.site.site_header = title
admin.site.index_title = subtitle

# Register your models here.
# Registrar modelo en el panel
admin.site.register(Page)