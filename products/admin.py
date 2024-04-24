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
        'display_categories',
        'price',
        'description',
        'thumb',  # Display thumbnail
    )

    def display_categories(self, obj):
        return ', '.join(category.name for category in obj.categories.all())

    ordering = ('sku',)
    prepopulated_fields = {"slug": ("name",)} 
    inlines = [ProductImageInline] 

    def thumb(self, obj):
        if obj.images.exists():
            image_url = obj.images.first().image.url
            return '<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(image_url)
        return 'No Image'

    thumb.allow_tags = True
    thumb.short_description = 'Thumbnail'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

admin.site.register(ProductImage) 


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Category, CategoryAdmin)