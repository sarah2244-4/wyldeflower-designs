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


class AddToWishlistForm(forms.ModelForm):
    product_id = forms.IntegerField(widget=forms.HiddenInput())

    def clean_product_id(self):
        product_id = self.cleaned_data.get('product_id')
        if not Product.objects.filter(id=product_id).exists():
            raise forms.ValidationError('Invalid product ID.')
        return product_id