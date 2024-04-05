from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    Prepoluate slug field
    """
    
    prepopulated_fields = {"slug": ("name",)} 

admin.site.register(Product, ProductAdmin)