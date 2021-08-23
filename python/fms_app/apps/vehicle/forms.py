from django import forms
from django.utils.translation import gettext_lazy as _

from .models import VehicleModel, VehicleCrModel, VehicleOrModel

class DateForm(forms.DateInput):
    input_type = 'date'

class VehicleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_vehicle_name(self):
        data = self.cleaned_data['vehicle_name']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_vehicle_type(self):
        data = self.cleaned_data['vehicle_type']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_position_assign(self):
        data = self.cleaned_data['position_assign']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_case_capacity(self):
        data = self.cleaned_data['case_capacity']
        
        if data <= 0:
            raise forms.ValidationError(_('* Determine the case capacity of the vehicle.'))
        return data

    def clean_aquisition_cost(self):
        data = self.cleaned_data['aquisition_cost']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_useful_life_month(self):
        data = self.cleaned_data['useful_life_month']
        
        if data <= 0:
            raise forms.ValidationError(_('* Determine the useful life in month of the vehicle.'))
        return data

    def clean_origin(self):
        data = self.cleaned_data['origin']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_status(self):
        data = self.cleaned_data['status']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_ownership(self):
        data = self.cleaned_data['ownership']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_area_coverage(self):
        data = self.cleaned_data['area_coverage']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    class Meta:
        model = VehicleModel
        fields = ('__all__')
        widgets = {
            'date_receive': DateForm(),
            'date_acquired': DateForm()
        }

class VehicleCrForm(forms.ModelForm):

    def __init__(self, fk = None, *args, **kwargs):
        super(VehicleCrForm, self).__init__(*args, **kwargs)

        self.fields['fk'].initial = fk

        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_field_office(self):
        data = self.cleaned_data['field_office']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_cr_no(self):
        data = self.cleaned_data['cr_no']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_mvfile_no(self):
        data = self.cleaned_data['mvfile_no']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_plate_no(self):
        data = self.cleaned_data['plate_no']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_engine_no(self):
        data = self.cleaned_data['engine_no']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_chasis_no(self):
        data = self.cleaned_data['chasis_no']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_denomination(self):
        data = self.cleaned_data['denomination']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_piston_displacement(self):
        data = self.cleaned_data['piston_displacement']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_no_cyclender(self):
        data = self.cleaned_data['no_cyclender']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_fuel_type(self):
        data = self.cleaned_data['fuel_type']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_make(self):
        data = self.cleaned_data['make']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_series(self):
        data = self.cleaned_data['series']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_body_no(self):
        data = self.cleaned_data['body_no']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_body_type(self):
        data = self.cleaned_data['body_type']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_year_model(self):
        data = self.cleaned_data['year_model']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_gross_weight(self):
        data = self.cleaned_data['gross_weight']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_shipping_weight(self):
        data = self.cleaned_data['shipping_weight']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_net_capacity(self):
        data = self.cleaned_data['net_capacity']
        
        if data <= 0:
            raise forms.ValidationError(_('* Determine the net capacity.'))
        return data

    def clean_owner(self):
        data = self.cleaned_data['owner']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_contact_no(self):
        data = self.cleaned_data['contact_no']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_address(self):
        data = self.cleaned_data['address']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_encumbered(self):
        data = self.cleaned_data['encumbered']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_details_f_registration(self):
        data = self.cleaned_data['details_f_registration']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_amount(self):
        data = self.cleaned_data['amount']
        
        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    class Meta:
        model = VehicleCrModel
        fields = ('fk', 'cr_no', 'date', 'field_office', 'chasis_no', 'engine_no', 'plate_no', 'mvfile_no', 'denomination', 'piston_displacement', 'no_cyclender', 'fuel_type', 'make', 'series', 'body_type', 'body_no', 'year_model', 'gross_weight', 'net_weight', 'shipping_weight', 'net_capacity', 'owner', 'contact_no', 'address', 'encumbered', 'details_f_registration', 'amount')
        widgets = {
            'date': DateForm(),
            'fk': forms.HiddenInput()
        }

class VehicleCreateOrForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VehicleCreateOrForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_date(self):
        data = self.cleaned_data['date']

        if data == '' or data == None:
            raise forms.ValidationError(_('* Date could not be empty.'))
        return data

    def clean_or_no(self):
        data = self.cleaned_data['or_no']

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    class Meta:
        model = VehicleOrModel
        fields = ('fk', 'date', 'or_no')
        widgets = {
            'fk': forms.HiddenInput(),
            'date': DateForm()
        }

class VehicleDetailsUpdateOrForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VehicleDetailsUpdateOrForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_or_no(self):
        data = self.cleaned_data['or_no']

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_field_office(self):
        data = self.cleaned_data['field_office']

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data
    
    def clean_address(self):
        data = self.cleaned_data['address']

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_transaction_no(self):
        data = self.cleaned_data['transaction_no']

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_posted_date(self):
        data = self.cleaned_data['posted_date']

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_private(self):
        data = self.cleaned_data['private']

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    def clean_file_no(self):
        data = self.cleaned_data['file_no']

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill.'))
        return data

    class Meta:
        model = VehicleOrModel
        fields = ('or_no', 'field_office', 'field_office_code', 'date', 'receive_from', 'address', 'transaction_no', 'posted_date', 'private', 'file_no')
        widgets = {
            'date': DateForm(),
            'posted_date': DateForm()
        }