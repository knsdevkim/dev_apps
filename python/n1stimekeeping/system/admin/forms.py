from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(AuthenticationForm):

    error_messages = {
        'invalid_login': 'Invalid credentials provided. Please correct your authenticate user or password.'
    }

    username = forms.CharField(label = 'Authenticate User', widget = forms.TextInput(), max_length = 20)
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput(), max_length = 100)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class GenerateReportForm(forms.Form):
    date_range_from = forms.DateField(label = 'Date From', widget = DateInput())
    date_range_to = forms.DateField(label = 'Date To', widget = DateInput())

    def __init__(self, *args, **kwargs):
        super(GenerateReportForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })