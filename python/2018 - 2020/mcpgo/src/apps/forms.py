from django import forms
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _


from .models import *


class LoginForm(AuthenticationForm):

    error_messages = {
        'invalid_login': 'Invalid auth user credentials.'
    }

    username = forms.CharField(label = 'Auth User', widget = forms.TextInput())
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_username(self):
        data = self.cleaned_data.get('username')
        if data == '':
            raise forms.ValidationError(_('*Fill auth username'))
        return data

    def clean_password(self):
        data = self.cleaned_data.get('password')
        if data == '':
            raise forms.ValidationError(_('*Provide password'))
        return data

    class Meta:
        model = Users


class SyncFileForm(forms.Form):
    refresh_data = forms.BooleanField(label = 'Remove old mcp and sync new one')
    filename     = forms.FileField(label = 'Sync MCP .xls', help_text = 'Choose file only have extension of <b>.xlsx</b>')

    def __init__(self, *args, **kwargs):
        super(SyncFileForm, self).__init__(*args, **kwargs)
        self.fields['filename'].widget.attrs.update({
            'accept': '.xlsx'
        })
        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class AccountForm(UserCreationForm):

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        if data == '':
            raise forms.ValidationError(_('What\'s your name?'))
        return data

    def clean_last_name(self):
        data = self.cleaned_data.get('last_name')
        if data == '':
            raise forms.ValidationError(_('What\'s your last name?'))
        return data

    def clean_link_mcp(self):
        data = self.cleaned_data.get('link_mcp')
        if data == '':
            raise forms.ValidationError(_('Make sure you have link mcp data to assign records to this account.'))
        return data

    def clean_email(self):
        data = self.cleaned_data.get('email')
        if data == '':
            raise forms.ValidationError(_('What\'s was the email address for this account?'))
        return data

    def clean_username(self):
        data = self.cleaned_data.get('username')
        if data == '':
            raise forms.ValidationError(_('Provide your username.'))
        return data

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)
        self.fields['first_name'].widget.attrs.update({
            'autofocus': True
        })
        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta(UserCreationForm.Meta):
        model  = Users
        fields = ('first_name', 'last_name', 'link_mcp', 'email', 'user_type', ) + UserCreationForm.Meta.fields
