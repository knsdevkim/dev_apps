from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import MediaModel, WebContentModel, ApplicationFormModel, DepartmentModel, JobPositionModel, JobQualificationModel

class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Invalid username or password.'
    }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-lg',
                'placeholder': field.upper()
            })

class NewsEventsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewsEventsForm, self).__init__(*args, **kwargs)

        self.fields['type'].initial = 'news_and_events'

        for field in self.fields:
            
            self.fields[field].required = False
            
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_title(self):
        data = self.cleaned_data.get('title')

        if data == '' or data == None:
            raise forms.ValidationError('Field is require to fill.')

        return data

    def clean_author(self):
        data = self.cleaned_data.get('author')

        if data == '' or data == None:
            raise forms.ValidationError('Field is require to fill.')

        return data

    def clean_location(self):
        data = self.cleaned_data.get('location')

        if data == '' or data == None:
            raise forms.ValidationError('Field is require to fill.')

        return data

    def clean_description(self):
        data = self.cleaned_data.get('description')

        if data == '' or data == None:
            raise forms.ValidationError('Field is require to fill.')

        return data

    def clean_ne_type(self):
        data = self.cleaned_data.get('ne_type')

        if data == '' or data == None:
            raise forms.ValidationError('Select an content type.')

        return data

    class Meta:
        model   = WebContentModel
        fields  = ['type', 'title', 'date_posted', 'author', 'location', 'video', 'description', 'ne_type']
        widgets = {
            'type': forms.HiddenInput(),
            'date_posted': DateInput()
        } 

class DepartmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            
            self.fields[field].required = False
            
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_title(self):
        data = self.cleaned_data.get('title')

        if data == '' or data == None:
            raise forms.ValidationError('Field is require to fill.')

        return data

    def clean_icon(self):
        data = self.cleaned_data.get('icon')

        if data == '' or data == None:
            raise forms.ValidationError('Field is require to fill.')

        return data

    def clean_description(self):
        data = self.cleaned_data.get('description')

        if data == '' or data == None:
            raise forms.ValidationError('Field is require to fill.')

        return data

    class Meta:
        model   = DepartmentModel
        fields  = ['title', 'icon', 'description']

class JobPositionForm(forms.ModelForm):

    def __init__(self, department_id = None, *args, **kwargs):
        super(JobPositionForm, self).__init__(*args, **kwargs)

        self.fields['department'].initial = department_id

        for field in self.fields:
            
            self.fields[field].required = False
            
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_title(self):
        data = self.cleaned_data.get('title')

        if data == '' or data == None:
            raise forms.ValidationError('Field is require to fill.')

        return data

    def clean_description(self):
        data = self.cleaned_data.get('description')

        if data == '' or data == None:
            raise forms.ValidationError('Field is require to fill.')

        return data

    class Meta:
        model   = JobPositionModel
        fields  = ['department', 'title', 'description', 'is_available']
        widgets = {
            'department': forms.HiddenInput()
        }

class JobQualificationForm(forms.ModelForm):

    def __init__(self, jobposition_id = None, *args, **kwargs):
        super(JobQualificationForm, self).__init__(*args, **kwargs)

        self.fields['jobposition'].initial = jobposition_id

        for field in self.fields:
            
            self.fields[field].required = False
            
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_title(self):
        data = self.cleaned_data.get('title')

        if data == '' or data == None:
            raise forms.ValidationError('Field is require to fill.')

        return data

    def clean_jobposition(self):
        data = self.cleaned_data.get('jobposition')

        if data == '' or data == None:
            raise forms.ValidationError('Field is require to fill.')

        return data

    def clean_content_type(self):
        data = self.cleaned_data.get('content_type')

        if data == '' or data == None:
            raise forms.ValidationError('Field is require to fill.')

        return data

    class Meta:
        model   = JobQualificationModel
        fields  = ['jobposition', 'title', 'content_type']
        widgets = {
            'jobposition': forms.HiddenInput()
        }

class ApplicationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        self.fields['type'].initial = 'apply_now'

    class Meta:
        model  = ApplicationFormModel
        fields = ['type', 'firstname', 'lastname', 'email', 'mobile', 'position', 'message', 'filename']
        widgets = {
            'type': forms.HiddenInput(),
            'message': forms.Textarea(attrs = {
                'class': 'materialize-textarea'
            })
        }

class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['type'].initial = 'contact_us'

    class Meta:
        model = ApplicationFormModel
        fields = ['type', 'firstname', 'lastname', 'email', 'concern', 'message']
        widgets = {
            'type': forms.HiddenInput(),
            'message': forms.Textarea(attrs = {
                'class': 'materialize-textarea'
            })
        }

class MediaForm(forms.Form):

    media_token = forms.CharField(max_length = 255, widget = forms.HiddenInput())
    filename    = forms.FileField(widget = forms.ClearableFileInput(attrs = { 'multiple': True }))

    def __init__(self, slug = None, token = None, *args, **kwargs):
        super(MediaForm, self).__init__(*args, **kwargs)
        
        self.fields['media_token'].initial = token