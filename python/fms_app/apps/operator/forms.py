from django import forms
from django.utils.translation import gettext_lazy as _

from .models import OPERATOR_TYPE, OperatorModel, ContactModel, DriverLicenseModel

class DateInput(forms.DateInput):
    input_type = 'date'

class OperatorDetailsForm(forms.ModelForm):

    operator_type = forms.ChoiceField(initial = 'driver', choices = OPERATOR_TYPE, widget = forms.RadioSelect(), help_text = 'For identification purposes.')

    def __init__(self, *args, **kwargs):
        super(OperatorDetailsForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False
            if field != 'operator_type':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

    def clean_employee_id(self):
        data = self.cleaned_data.get('employee_id')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    def clean_firstname(self):
        data = self.cleaned_data.get('firstname')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    def clean_lastname(self):
        data = self.cleaned_data.get('lastname')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    def clean_middlename(self):
        data = self.cleaned_data.get('middlename')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    def clean_address(self):
        data = self.cleaned_data.get('address')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    def clean_contact_no(self):
        data = self.cleaned_data.get('contact_no')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    def clean_email(self):
        data = self.cleaned_data.get('email')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    def clean_position(self):
        data = self.cleaned_data.get('position')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    def clean_area(self):
        data = self.cleaned_data.get('area')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    def clean_operator_type(self):
        data = self.cleaned_data.get('operator_type')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    class Meta:
        model = OperatorModel
        fields = ('__all__')
        widgets = {
            'date_employed': DateInput(),
            'birthdate': DateInput()
        }

class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_fullname(self):
        data = self.cleaned_data.get('fullname')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    def clean_address(self):
        data = self.cleaned_data.get('address')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    def clean_contact_no(self):
        data = self.cleaned_data.get('contact_no')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    def clean_relation(self):
        data = self.cleaned_data.get('relation')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))
        return data

    class Meta:
        model = ContactModel
        fields = ('__all__')

class DriverLicenseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DriverLicenseForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = DriverLicenseModel
        fields = ('license_no', 'restriction', 'agency_code', 'expiration_date')
        widgets = {
            'expiration_date': DateInput()
        }