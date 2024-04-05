from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=50)


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Item(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    size = models.CharField(max_length=25, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.item_name

        