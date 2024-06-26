from django import forms

from .models import Product, Category, ProductImage


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].widget.attrs['multiple'] = True
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.products():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']