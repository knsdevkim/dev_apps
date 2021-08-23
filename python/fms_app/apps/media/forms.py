from django import forms
from django.utils.translation import gettext_lazy as _

from .models import MediaModel, DocumentModel

class MediaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MediaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = ''
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'dropzone'
            })

    def clean_media_file(self):
        data = self.cleaned_data['media_file']

        if data == '' or data == None:
            raise forms.ValidationError('Please select an image.')
        return data

    class Meta:
        model = MediaModel
        fields = ('media_file',)

class DocumentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_document_name(self):
        data = self.cleaned_data.get('document_name')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))

        return data

    def clean_media_file(self):
        data = self.cleaned_data.get('media_file')

        if data == '' or data == None:
            raise forms.ValidationError(_('* Require to fill'))

        return data

    class Meta:
        model = DocumentModel
        fields = ('__all__')