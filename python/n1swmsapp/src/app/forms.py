from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class LoginUserForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Invalid credentials.'
    }

    username = forms.CharField(label = 'N1S AUTHORIZE USER', max_length = 150, widget = forms.TextInput())
    password = forms.CharField(label = 'Password', max_length = 150, widget = forms.PasswordInput())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Users


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)
        self.fields['first_name'].widget.attrs.update({'autofocus': ''})
        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        if data == '':
            raise forms.ValidationError(_('What is the first name of the new admin?'))
        return data

    def clean_last_name(self):
        data = self.cleaned_data.get('last_name')
        if data == '':
            raise forms.ValidationError(_('What is the last name of the new admin?'))
        return data

    def clean_employee_code(self):
        data = self.cleaned_data.get('employee_code')
        if data == '':
            raise forms.ValidationError(_('What is the employee ID number?'))
        return data

    def clean_gender(self):
        data = self.cleaned_data.get('gender')
        if data == '':
            raise forms.ValidationError(_('Select new user gender.'))
        return data

    def clean_address(self):
        data = self.cleaned_data.get('address')
        if data == '':
            raise forms.ValidationError(_('State new user address.'))
        return data

    def clean_email(self):
        data = self.cleaned_data.get('email')
        if data == '':
            raise forms.ValidationError(_('Provide email address.'))


    class Meta(UserCreationForm.Meta):
        model  = Users
        fields = ('first_name', 'last_name', 'employee_code', 'gender', 'auth_level', 'address', 'email',) + UserCreationForm.Meta.fields


class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        if data == '':
            raise forms.ValidationError(_('* Fill this input to modify!'))
        return data

    def clean_last_name(self):
        data = self.cleaned_data.get('last_name')
        if data == '':
            raise forms.ValidationError(_('* Fill this input to modify!'))
        return data

    def clean_employee_code(self):
        data = self.cleaned_data.get('employee_code')
        if data == '':
            raise forms.ValidationError(_('* Fill this input to modify!'))
        return data

    def clean_gender(self):
        data = self.cleaned_data.get('gender')
        if data == '':
            raise forms.ValidationError(_('* Fill this input to modify!'))
        return data

    def clean_address(self):
        data = self.cleaned_data.get('address')
        if data == '':
            raise forms.ValidationError(_('* Fill this input to modify!'))
        return data

    class Meta:
        model  = Users
        fields = ('first_name', 'last_name', 'employee_code', 'gender', 'address')

class SyncForm(forms.Form):
    foldername = forms.CharField(label = 'Folder Name', max_length = 150, widget = forms.TextInput())
    fileinput  = forms.FileField(label = 'File', help_text = 'Use only and only <strong>.xlsx</strong> format of excel to upload!')

    def __init__(self, *args, **kwargs):
        super(SyncForm, self).__init__(*args, **kwargs)
        self.fields['fileinput'].widget.attrs.update({
            'accept': '.xlsx'
        })
        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_foldername(self):
        data = self.cleaned_data.get('foldername')
        if data == '':
            raise forms.ValidationError(_('What will be the folder?'))
        return data

    def clean_fileinput(self):
        data = self.cleaned_data.get('fileinput')
        if data == '':
            raise forms.ValidationError(_('It requires file excel to upload and sync data.'))
        return data
