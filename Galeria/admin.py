from django.contrib import admin
from .models import *  # Import your Usuario model
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')  # Customize the displayed fields in the list view
    list_filter = ('nombre', 'apellido')  # Add filters for fields in the right sidebar
    search_fields = ('nombre', 'apellido', 'email')  # Add a search bar for these fields
    list_per_page = 20  # Set the number of items displayed per page

admin.site.register(Usuario, UsuarioAdmin)  # Register the model with the customized admin class
