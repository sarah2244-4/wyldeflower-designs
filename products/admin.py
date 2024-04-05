from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Prepoluate slug field
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'description',
        'thumb',
        'image',
        'size',
    )

    ordering = ('sku',)
    
    prepopulated_fields = {"slug": ("name",)} 


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Category, CategoryAdmin)