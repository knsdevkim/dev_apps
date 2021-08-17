from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .models import *

'''
    @class -> Helpers widget
'''
class DateInput(forms.DateInput):
    input_type = 'date'

'''
    @class: UpdateUserForm
        -> Update user information form.
'''
class UpdateUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


'''
    @class: LoginForm
        -> Login form
'''
class LoginForm(AuthenticationForm):
    # Error messages collection.
    error_messages = {
        'invalid_login': 'Invalid username or password.'
    }

    # Widgets
    username = forms.CharField(max_length=100, widget=forms.TextInput())
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())

    # Add more attribute in the widget.
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class PasswordChangeForm(PasswordChangeForm):
    error_messages = {
        'password_incorrect': 'Invalid old password.',
        'password_mismatch': 'New password is mismatch with the confirm password.'
    }

    old_password = forms.CharField(label='Current Password', max_length = 150, widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='New Password', max_length = 150, widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Confirm New Password', max_length = 150, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].help_text = 'For high security password it is suggested with 8 characters length atleast 1 uppercase character and atleast 1 special character within your password characters.'

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

'''
    @class: SlideshowForm
        -> Slideshow form
'''
class SlideshowForm(forms.ModelForm):
    # Add more attribute in the widget
    def __init__(self, *args, **kwargs):
        super(SlideshowForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['title'].required = False
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    # Table and field to access
    class Meta:
        model = SlideshowModel
        fields = '__all__'
        widgets = {
            'description': forms.Textarea
        }

'''
    @class: AboutForm
        -> about form
'''
class AboutForm(forms.ModelForm):
    # Add more attribute in the widget.
    def __init__(self, *args, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    # Table and field to access
    class Meta:
        model = AboutModel
        fields = '__all__'
'''
    @class: BranchForm
        -> Branch form
'''
class BranchForm(forms.ModelForm):
    # Add more attribute in the widget
    def __init__(self, *args, **kwargs):
        super(BranchForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    # Table and field to access
    class Meta:
        model = BranchModel
        fields = '__all__'

'''
    @class: NewsEventForm
        -> News and Event form
'''
class NewsEventForm(forms.ModelForm):
    # Add more attribute in widget
    def __init__(self, *args, **kwargs):
        super(NewsEventForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    # Table and field to access.
    class Meta:
        model = NewsEventModel
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }

'''
    @class: MilestoneForm
        -> Milestone form
'''
class MilestoneForm(forms.ModelForm):
    # Add more attribute in widget
    def __init__(self, *args, **kwargs):
        super(MilestoneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    # Table and field in database
    class Meta:
        model = MilestoneModel
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }

'''
    @class: VideoForm
        -> VideoForm
'''
class VideoForm(forms.ModelForm):
    # Add more attribute in widget
    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['video'].widget.attrs.update({
            'accept': 'video/*'
        })
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    # Table and field in database.
    class Meta:
        model = VideoModel
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }

'''
    @class: CareersForm
        -> Careers form
'''
class CareersForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CareersForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    # Table and field in database
    class Meta:
        model = CareersModel
        fields = '__all__'

'''
    @class: ContactusForm
        -> contact us form
'''
class ContactusForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = ContactusModel
        fields = '__all__'
