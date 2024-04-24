from django.contrib import admin
from .models import Product, Category, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of extra empty forms to display for adding images

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'description',
        'thumb',  # Display thumbnail
        'size',
    )
    ordering = ('sku',)
    prepopulated_fields = {"slug": ("name",)} 
    inlines = [ProductImageInline]  # Include ProductImageInline in ProductAdmin

    def thumb(self, obj):
        if obj.images.exists():  # Check if product has associated images
            image_url = obj.images.first().image.url
            return '<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(image_url)
        return 'No Image'

    thumb.allow_tags = True
    thumb.short_description = 'Thumbnail'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Add custom logic here if needed

admin.site.register(ProductImage)  # Register ProductImage model in admin



class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Category, CategoryAdmin)