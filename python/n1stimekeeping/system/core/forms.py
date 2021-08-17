from django import forms


class TimeLogForm(forms.Form):
    time = forms.CharField(widget=forms.HiddenInput())
    employee_id = forms.CharField(label='Employee ID', widget=forms.TextInput(attrs={
        'autofocus': ''
    }), max_length=6)

    def __init__(self, *args, **kwargs):
        super(TimeLogForm, self).__init__(*args, **kwargs)

        self.fields['time'].widget.attrs['readonly'] = True

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class SyncFileForm(forms.Form):
    file = forms.FileField(label='Upload xls file.')
