from django import forms

from .models import Product, Category, ProductImage

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class ProductForm(forms.ModelForm):

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    cover_image = forms.ImageField(label='Select Cover Image', required=True)
    images = MultipleFileField(label='Select Listing Images', required=False)

    class Meta:
        model = Product
        fields = ['sku', 'name', 'price', 'description', 'categories', 'cover_image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].label_from_instance = lambda obj: obj.get_friendly_name()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
