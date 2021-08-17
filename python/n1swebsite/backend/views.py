from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from .forms import *
from .models import *

# Create your views here.

'''
    @method: listView
        -> Displaying specific model base on the pathfind passes in URL.
'''
@login_required
def listView(request, pathfind):
    # Set the template base on the pathfind passes in the URL.
    template_name = f'components/crud/view.html'
    # Variable for setting specific model base on the pathfind parameter.
    model = None
    # Check what pathfind passes and give specific model on that path.
    if pathfind == 'slideshow':
        model = SlideshowModel.objects.all()
    elif pathfind == 'branch':
        model = BranchModel.objects.all()
    elif pathfind == 'about':
        model = AboutModel.objects.get(id = 1)
    elif pathfind == 'milestone':
        model = MilestoneModel.objects.all()
    elif pathfind == 'newsevent':
        model = NewsEventModel.objects.all()
    elif pathfind == 'video':
        model = VideoModel.objects.all()
    elif pathfind == 'site':
        model = SiteSettingsModel.objects.all()
    elif pathfind == 'careers':
        model = CareersModel.objects.all()
    elif pathfind == 'feeds':
        model = ContactusModel.objects.all()

    return render(request, template_name, {
        'object': model,
        'context_title': pathfind
    })

'''
    @method: setSlideshow
        -> Set slideshow to In use.
'''
@login_required
def setSlideshow(request):
    # Set to unuse all the objects.
    SlideshowModel.setUnuse()
    # Check if there is a post request.
    if request.method == 'POST':
        ids = [int(id) for id in request.POST.getlist('id')]
        # Set the checked one to In Use
        SlideshowModel.objects.filter(id__in = ids).update(
            status = 'In Use'
        )
        # Show message in UI.
        messages.success(request, 'Successfully set.')
        return redirect('backend:listview', pathfind = 'slideshow')
    return redirect('backend:listview', pathfind = 'slideshow')

'''
    @method: setSiteSettings
        -> Set site settings display
'''
@login_required
def setSiteSettings(request):
    # Set to false all objects display
    SiteSettingsModel.updateallsettings()
    # Check if there is a post request.
    if request.method == 'POST':
        ids = [int(id) for id in request.POST.getlist('id')]
        SiteSettingsModel.objects.filter(id__in = ids).update(
            is_display = True
        )
        messages.success(request, 'Successfully updated.')
        return redirect('backend:listview', pathfind = 'site')
    return redirect('backend:listview', pathfind = 'site')

'''
    @class: UpdateUserInfo
        -> Update user info view.
'''
class UpdateUserInfo(LoginRequiredMixin, UpdateView):
    template_name = 'components/crud/update.html'
    form_class = UpdateUserForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Update Admin Information'
        kwargs['context_button_label'] = 'Update'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Admin information has been modified.')
        return super().form_valid(form)

    def get_object(self, queryset = None):
        return User.objects.get(pk = self.request.user.pk)

    def get_success_url(self):
        return reverse_lazy('backend:updateuser')


'''
    @class: SettingsView
        -> Settings in admin panel.
'''
class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'components/settings/view.html'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Settings'
        return super().get_context_data(**kwargs)

'''
    @class: RendererLoginView
        -> For login view and processing.
'''
class RendererLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'components/login/view.html'

'''
    @class: RendererChangePasswordView
        -> For changing password view and processing.
'''
class RendererChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'components/login/changepassword.html'
    form_class = PasswordChangeForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Change Password'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Password is successfully updated.')
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('backend:changepassword')

'''
    @class: RendererLogoutView
        -> For logging out account.
'''
class RendererLogoutView(LogoutView):
    pass

'''
    @class: RendererDashboardView
        -> For dashboard admin panel.
'''
class RendererDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'components/dashboard/view.html'

    # Set context to access in template.
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'dashboard'
        return super().get_context_data(**kwargs)

'''
    @class: CreateSlideshow
        -> Creating slideshow object
'''
class CreateSlideshow(LoginRequiredMixin, CreateView):
    template_name = 'components/crud/create.html'
    form_class = SlideshowForm

    # Set context to access in template
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'create slideshow'
        kwargs['context_button_label'] = 'Create'
        return super().get_context_data(**kwargs)

    # If form is valid save the object then show success message to UI.
    def form_valid(self, form):
        # Save object
        self.object = form.save()
        # Message
        messages.success(self.request, 'Successfully added.')
        return super().form_valid(form)

    # Redirect the page by its path.
    def get_success_url(self):
        return reverse_lazy('backend:createslideshow')

'''
    @class: EditSlideshow
        -> Modify field of the object slideshow
'''
class UpdateSlideshow(LoginRequiredMixin, UpdateView):
    template_name = 'components/crud/update.html'
    form_class = SlideshowForm

    # Set context to access in template
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'update slideshow'
        kwargs['context_button_label'] = 'Update'
        return super().get_context_data(**kwargs)

    # Get the object
    def get_queryset(self):
        return SlideshowModel.objects.filter(id = self.kwargs['pk'])

    # If form is valid update the object then show success message to UI.
    def form_valid(self, form):
        # Save object
        self.object = form.save()
        # Message
        messages.success(self.request, 'Successfully update!')
        return super().form_valid(form)

    # Redirect the page by its path.
    def get_success_url(self):
        return reverse_lazy('backend:updateslideshow', kwargs = {
            'pk': self.kwargs['pk']
        })

'''
    @class: DeleteSlideshow
        -> Delete the field of the object slideshow
'''
class DeleteSlideshow(LoginRequiredMixin, DeleteView):
    model = SlideshowModel
    template_name = None

    # Redirect the page by its path with success message.
    def get_success_url(self):
        messages.success(self.request, 'Successfully deleted.')
        return reverse_lazy('backend:listview', kwargs = {
            'pathfind': 'slideshow'
        })

'''
    @class: UpdateAbout
        -> Modifying about content
'''
class UpdateAbout(LoginRequiredMixin, UpdateView):
    template_name = 'components/crud/update.html'
    form_class = AboutForm
    context_object_name = 'object'

    # Set context to access in template
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'update about'
        kwargs['context_button_label'] = 'Update'
        return super().get_context_data(**kwargs)

    # Get the object from the table
    def get_queryset(self):
        return AboutModel.objects.filter(id = self.kwargs['pk'])

    # If form is valid then update the object and show message to UI.
    def form_valid(self, form):
        # Save the object
        self.object = form.save()
        # Show the message to UI.
        messages.success(self.request, 'Successfully update.')
        return super().form_valid(form)

    # Return to its path with parameter PK.
    def get_success_url(self):
        return reverse_lazy('backend:updateabout', kwargs = {
            'pk': self.kwargs['pk']
        })

'''
    @class: CreateBranch
        -> Creating branch object.
'''
class CreateBranch(LoginRequiredMixin, CreateView):
    template_name = 'components/crud/create.html'
    form_class = BranchForm

    # Set context to access in form
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'create branch'
        kwargs['context_button_label'] = 'Create'
        return super().get_context_data(**kwargs)

    # If form is valid create the object.
    def form_valid(self, form):
        # Save the object
        self.object = form.save()
        # Show the message to UI.
        messages.success(self.request, 'Successfully created.')
        return super().form_valid(form)

    # Redirect to its path.
    def get_success_url(self):
        return reverse_lazy('backend:createbranch')

'''
    @class: DetailsBranch
        -> Details of the object branch.
'''
class DetailsBranch(LoginRequiredMixin, DetailView):
    model = BranchModel
    template_name = 'components/crud/details.html'
    context_object_name = 'object'

    # Set context to access in template.
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Branch Details'
        return super().get_context_data(**kwargs)

    # Get the object
    def get_queryset(self):
        return self.model.objects.filter(id = self.kwargs['pk'])

'''
    @class: UpdateBranch
        -> Updating the branch objects.
'''
class UpdateBranch(LoginRequiredMixin, UpdateView):
    template_name = 'components/crud/update.html'
    form_class = BranchForm
    context_object_name = 'object'

    # Set context to access in template
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'update branch'
        kwargs['context_button_label'] = 'Update'
        return super().get_context_data(**kwargs)

    # Get the object from the table.
    def get_queryset(self):
        return BranchModel.objects.filter(id = self.kwargs['pk'])

    # If form is valid update the object.
    def form_valid(self, form):
        # Save the object
        self.object = form.save()
        # Show the message to UI.
        messages.success(self.request, 'Successfully updated.')
        return super().form_valid(form)

    # Redirect to its path with PK.
    def get_success_url(self):
        return reverse_lazy('backend:updatebranch', kwargs = {
            'pk': self.kwargs['pk']
        })

'''
    @class: DeleteBranch
        -> Deleting branch object to database.
'''
class DeleteBranch(LoginRequiredMixin, DeleteView):
    model = BranchModel
    template_name = None

    # Redirect to its path.
    def get_success_url(self):
        messages.success(self.request, 'Sucessfully deleted.')
        return reverse_lazy('backend:listview', kwargs = {
            'pathfind': 'branch'
        })

'''
    @class: CreateMilestone
        -> Creating milestone object
'''
class CreateMilestone(LoginRequiredMixin, CreateView):
    template_name = 'components/crud/create.html'
    form_class = MilestoneForm

    # Set context to access in template
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'create milestone'
        kwargs['context_button_label'] = 'Create'
        return super().get_context_data(**kwargs)

    # If the form is valid then create the object.
    def form_valid(self, form):
        # Save the object
        self.object = form.save()
        # Show the message in the UI.
        messages.success(self.request, 'Successfully created.')
        return super().form_valid(form)

    # Redirect to its path.
    def get_success_url(self):
        return reverse_lazy('backend:createmilestone')

'''
    @class: DetailsMilestone
        -> Details of the object of milestone.
'''
class DetailsMilestone(LoginRequiredMixin, DetailView):
    model = MilestoneModel
    template_name = 'components/crud/details.html'
    context_object_name = 'object'

    # Set context to access in template.
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Milestone Details'
        return super().get_context_data(**kwargs)

    # Get the object
    def get_queryset(self):
        return self.model.objects.filter(id = self.kwargs['pk'])

'''
    @class: UpdateMilestone
        -> Updating the object of milestone
'''
class UpdateMilestone(LoginRequiredMixin, UpdateView):
    template_name = 'components/crud/update.html'
    form_class = MilestoneForm
    context_object_name = 'object'

    # Set context to access in template
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'update milestone'
        kwargs['context_button_label'] = 'Update'
        return super().get_context_data(**kwargs)

    # Get the object of milestone.
    def get_queryset(self):
        return MilestoneModel.objects.filter(id = self.kwargs['pk'])

    # If the form is valid then update the object.
    def form_valid(self, form):
        # Save the object.
        self.object = form.save()
        # Show message in the UI.
        messages.success(self.request, 'Successfully updated.')
        return super().form_valid(form)

    # Redirect to its path.
    def get_success_url(self):
        return reverse_lazy('backend:updatemilestone', kwargs = {
            'pk': self.kwargs['pk']
        })

'''
    @class: DeleteMilestone
        -> Deleting the milestone object.
'''
class DeleteMilestone(LoginRequiredMixin, DeleteView):
    model = MilestoneModel
    template_name = None

    # Redirect to its list view path.
    def get_success_url(self):
        messages.success(self.request, 'Sucessfully deleted.')
        return reverse_lazy('backend:listview', kwargs = {
            'pathfind': 'milestone'
        })

'''
    @class: CreateNewsEvent
        -> Creating object of news and event.
'''
class CreateNewsEvent(LoginRequiredMixin, CreateView):
    template_name = 'components/crud/create.html'
    form_class = NewsEventForm

    # Set context to access in template
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'create news and event'
        kwargs['context_button_label'] = 'Create'
        return super().get_context_data(**kwargs)

    # If form is valid then create the object.
    def form_valid(self, form):
        # Save the object
        self.object = form.save()
        # Show the message to UI.
        messages.success(self.request, 'Successfully create')
        return super().form_valid(form)

    # Redirect to its path
    def get_success_url(self):
        return reverse_lazy('backend:createnewsevent')

'''
    @class: DetailsNewsEvent
        -> Details of the object of news and event.
'''
class DetailsNewsEvent(LoginRequiredMixin, DetailView):
    model = NewsEventModel
    template_name = 'components/crud/details.html'
    context_object_name = 'object'

    # Set context to access in template.
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'News &amp; Event Details'
        return super().get_context_data(**kwargs)

    # Get the objects
    def get_queryset(self):
        return self.model.objects.filter(id = self.kwargs['pk'])

'''
    @class: UpdateNewsEvent
        -> Updating the object of news and event.
'''
class UpdateNewsEvent(LoginRequiredMixin, UpdateView):
    template_name = 'components/crud/update.html'
    form_class = NewsEventForm
    context_object_name = 'object'

    # Set context to access in template.
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'update news and event'
        kwargs['context_button_label'] = 'Update'
        return super().get_context_data(**kwargs)

    # Get the object
    def get_queryset(self):
        return NewsEventModel.objects.filter(id = self.kwargs['pk'])

    # If the form is valid then update the object
    def form_valid(self, form):
        # Save the object
        self.object = form.save()
        # Show the message to UI.
        messages.success(self.request, 'Successfully update.')
        return super().form_valid(form)

    # Redirect to its path
    def get_success_url(self):
        return reverse_lazy('backend:updatenewsevent', kwargs = {
            'pk': self.kwargs['pk']
        })

'''
    @class: DeleteNewsEvent
        -> Deleting the news and event object.
'''
class DeleteNewsEvent(LoginRequiredMixin, DeleteView):
    model = NewsEventModel
    template_name = None

    # Return to the listview path.
    def get_success_url(self):
        messages.success(self.request, 'Sucessfully deleted.')
        return reverse_lazy('backend:listview', kwargs = {
            'pathfind': 'newsevent'
        })

'''
    @class: CreateVideo
        -> Create video object.
'''
class CreateVideo(LoginRequiredMixin, CreateView):
    template_name = 'components/crud/create.html'
    form_class = VideoForm

    # Set context to access in template UI.
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'create video content'
        kwargs['context_button_label'] = 'Create'
        return super().get_context_data(**kwargs)

    # If form is valid then create the object
    def form_valid(self, form):
        # Save the object.
        self.object = form.save()
        # Show message in UI.
        messages.success(self.request, 'Successfully created.')
        return super().form_valid(form)

    # Redirect to its path
    def get_success_url(self):
        return reverse_lazy('backend:createvideo')

'''
    @class: UpdateVideo
        -> Update video object.
'''
class UpdateVideo(LoginRequiredMixin, UpdateView):
    model = VideoModel
    template_name = 'components/crud/update.html'
    form_class = VideoForm
    context_object_name = 'object'

    # Set the context to access in the template
    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'update video content'
        kwargs['context_button_label'] = 'Update'
        return super().get_context_data(**kwargs)

    # Get the object to be update
    def get_queryset(self):
        return self.model.objects.filter(id = self.kwargs['pk'])

    # If the form is valid save the object.
    def form_valid(self, form):
        # Update the object
        self.object = form.save()
        # Show the message in the UI.
        messages.success(self.request, 'Successfully update.')
        return super().form_valid(form)

    # Redirect to its path
    def get_success_url(self):
        return reverse_lazy('backend:updatevideo', kwargs = {
            'pk': self.kwargs['pk']
        })

'''
    @class: DeleteVideo
        -> Delete video object
'''
class DeleteVideo(LoginRequiredMixin, DeleteView):
    model = VideoModel
    template_name = None

    # Redirect to its path with message.
    def get_success_url(self):
        messages.success(self.request, 'Successfully delete.')
        return reverse_lazy('backend:listview', kwargs = {
            'pathfind': 'video'
        })

'''
    @class: CreateCareers
        -> Creating careers
'''
class CreateCareers(LoginRequiredMixin, CreateView):
    template_name = 'components/crud/create.html'
    form_class = CareersForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Create Careers'
        kwargs['context_button_label'] = 'Create'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        # Save the object
        self.object = form.save()
        # Show message in UI
        messages.success(self.request, 'Successfully created.')
        return super().form_valid(form)

    # Redirect to its path
    def get_success_url(self):
        return reverse_lazy('backend:createcareers')

'''
    @class: UpdateCareers
        -> Update career objects.
'''
class UpdateCareers(LoginRequiredMixin, UpdateView):
    model = CareersModel
    template_name = 'components/crud/update.html'
    form_class = CareersForm
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Update Careers'
        kwargs['context_button_label'] = 'Update'
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.filter(pk = self.kwargs[self.pk_url_kwarg])

    def form_valid(self, form):
        # Save the object modify
        self.object = form.save()
        # Show message to UI.
        messages.success(self.request, 'Successfully update.')
        return super().form_valid(form)

    # Redirect to its path.
    def get_success_url(self):
        return reverse_lazy('backend:updatecareers', kwargs = {
            'pk': self.kwargs[self.pk_url_kwarg]
        })

'''
    @class: DeleteCareers
        -> Delete careers object
'''
class DeleteCareers(LoginRequiredMixin, DeleteView):
    model = CareersModel
    template_name = None

    # Redirect to its path
    def get_success_url(self):
        messages.success(self.request, 'Successfully deleted.')
        return reverse_lazy('backend:listview', kwargs = {
            'pathfind': 'careers'
        })

'''
    @class: DeleteContactus
        -> Create contact objects.
'''
class DeleteContactus(LoginRequiredMixin, DeleteView):
    model = ContactusModel
    template_name = None

    def get_success_url(self):
        return reverse_lazy('backend:listview', kwargs = {
            'pathfind': 'contactus'
        })
