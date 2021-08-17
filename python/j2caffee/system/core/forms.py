from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class DoughForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DoughForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = DoughModel
        fields = '__all__'

class LoginForm(AuthenticationForm):
    username = forms.CharField(label = 'Authenticate User', widget = forms.TextInput())
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ProductCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductCategoryForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = ProductCategoryModel
        fields = '__all__'

class ProductsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductsForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = ProductsModel
        fields = '__all__'

class ProductUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductUpdateForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = ProductsModel
        fields = ['category', 'product_name', 'price', 'online_price', 'dough']

class DoughUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DoughUpdateForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = DoughModel
        fields = ['dough']

class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = OrderModel
        fields = ['qty']

class GenerateReportsForm(forms.Form):
    date_range_from = forms.DateField(label = 'Date From', widget = DateInput())
    date_range_to = forms.DateField(label = 'Date To', widget = DateInput())

    def __init__(self, *args, **kwargs):
        super(GenerateReportsForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = ExpenseModel
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }

class ProductLogForm(forms.Form):
    STATUS_OPTION = [
        ('ADDED', 'ADD'),
        ('REMOVED', 'REMOVE')
    ]

    qty = forms.IntegerField(label = 'Qty')
    status = forms.ChoiceField(label = 'Status', widget = forms.Select(), choices = STATUS_OPTION)

    def __init__(self, *args, **kwargs):
        super(ProductLogForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class DoughLogForm(forms.Form):
    STATUS_OPTION = [
        ('ADDED', 'ADD'),
        ('REMOVED', 'REMOVE')
    ]

    qty = forms.FloatField(label = 'Qty')
    status = forms.ChoiceField(label = 'Status', widget = forms.Select(), choices = STATUS_OPTION)

    def __init__(self, *args, **kwargs):
        super(DoughLogForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class TableForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TableForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = TableModel
        fields = '__all__'


class DiscountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DiscountForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
            model = DiscountModel
            fields = '__all__'
