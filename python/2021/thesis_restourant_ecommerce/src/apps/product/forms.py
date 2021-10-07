from django import forms

from .models import ProductModel

class ProductForm(forms.ModelForm):
    image = forms.ImageField()

    def __init__(self, category, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['category_fk'].initial = category
        

    class Meta:
        model   = ProductModel
        fields  = ('__all__')
        widgets = {
            'category_fk': forms.HiddenInput()
        }
