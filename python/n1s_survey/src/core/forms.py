from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _

from core.models import Users


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Invalid username or password.'
    }

    username = forms.CharField(max_length = 100, widget = forms.TextInput())
    password = forms.CharField(max_length = 250, widget = forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['password'].required = False
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_username(self):
        data = self.cleaned_data.get('username')
        if data == '':
            raise forms.ValidationError(_('Username is require to fill!'))
        return data

    def clean_password(self):
        data = self.cleaned_data.get('password')
        if data == '':
            raise forms.ValidationError(_('Password is require to fill!'))
        return data

    class Meta:
        model  = Users
