from django import forms
from .models import *

class UploadForm(forms.Form):
    RECORD_TYPE_OPTIONS = [
        ('', '-------------------------'),
        ('ada', 'AUTOMATIC DEDUCTION ADVICE'),
        ('itequipment', 'IT EQUIPMENT / SFA SELLING TOOLS ASSIGNMENT FORM')
    ]

    folder = forms.CharField(label = 'Folder Name', max_length = 150, widget = forms.TextInput())
    type_record = forms.ChoiceField(label = 'Folder Type', choices = RECORD_TYPE_OPTIONS, widget = forms.Select())
    file = forms.FileField(label = 'Upload File', help_text = 'It is highly required to name your sheet as <i>"Sheet1"</i> to read. And also the columns must be pattern to the require pattern instructed by the developer.')

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class FolderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FolderForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = FolderModel
        fields = ['folder', 'type_record']

class AdaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = AdaModel
        fields = '__all__'

class ItEquipmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItEquipmentForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = ItEquipmentModel
        fields = '__all__'