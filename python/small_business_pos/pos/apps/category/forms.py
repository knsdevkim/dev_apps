from django import forms
from django.utils.translation import gettext_lazy as _

from .models import CategoryModel

class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_name(self):
        data = self.cleaned_data.get('name')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))

        return data

    class Meta:
        model  = CategoryModel
        fields = ('__all__')