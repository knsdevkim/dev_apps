from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models.functions import TruncMonth
from django.db.models import Sum

# views generic template
from django.views.generic import CreateView, DeleteView, ListView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

# models
from .models import WebContentModel, ApplicationFormModel, MediaModel, WebAnalyticsModel

# forms
from .forms import *

# decorators
from .decorators import *

# Create your views here.

# Update visibility of job
@login_required
def update_job_visibilty(request, slug, parent_id, visibility, pk):
    is_available = True if visibility == 'show' else False
    JobPositionModel.objects.filter(pk = pk).update(is_available = is_available)
    return redirect(reverse('apps:jobpositionlistview', kwargs = {
        'slug': slug,
        'id': parent_id
    }))

# DASHBOARD

@login_required
def dashboard(request):
    context = {}
    return render(request, 'components/dashboard/index.html', context = context)

method_decorator(is_authenticated, name = 'dispatch')
class LoginViewTemplate(LoginView):
    template_name = 'login/index.html'
    authentication_form = LoginForm

class LogoutViewTemplate(LogoutView):
    pass

# LIST VIEWS

@method_decorator(is_unauthenticated, name = 'dispatch')
class WebAnalyticViewModule(LoginRequiredMixin, ListView):
    model               = WebAnalyticsModel
    template_name       = 'components/list/index.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['analysis_visitor'] = WebAnalyticsModel.objects\
        .annotate(month = TruncMonth('date_visited'))\
        .values('month')\
        .annotate(total_sum=Sum('visit_count'))\
        .values('month', 'total_sum');
        kwargs['token_view'] = self.kwargs.get('slug')
        kwargs['slug'] = 'analytic'
        return super(WebAnalyticViewModule, self).get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.all()

@method_decorator(is_unauthenticated, name = 'dispatch')
class ListViewModule(LoginRequiredMixin, ListView):
    model               = WebContentModel
    template_name       = 'components/list/index.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['token_view'] = self.kwargs.get('slug')
        kwargs['slug'] = 'web'
        return super(ListViewModule, self).get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.all()

@method_decorator(is_unauthenticated, name = 'dispatch')
class DepartmentListView(LoginRequiredMixin, ListView):
    model               = DepartmentModel
    template_name       = 'components/list/index.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['token_view'] = self.kwargs.get('slug')
        kwargs['slug'] = 'department'
        return super(DepartmentListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.all()

@method_decorator(is_unauthenticated, name = 'dispatch')
class JobPositionListView(LoginRequiredMixin, ListView):
    model               = JobPositionModel
    template_name       = 'components/list/index.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['token_view'] = self.kwargs.get('slug')
        kwargs['slug'] = 'jobposition'
        kwargs['department_id'] = self.kwargs.get('id')
        return super(JobPositionListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.filter(department = self.kwargs.get('id'))

@method_decorator(is_unauthenticated, name = 'dispatch')
class JobQualificationListView(LoginRequiredMixin, ListView):
    model               = JobQualificationModel
    template_name       = 'components/list/index.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['token_view'] = self.kwargs.get('slug')
        kwargs['slug'] = 'jobqualification'
        kwargs['jobposition_id'] = self.kwargs.get('id')
        return super(JobQualificationListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.filter(jobposition = self.kwargs.get('id'))

@method_decorator(is_unauthenticated, name = 'dispatch')
class ApplicationListView(LoginRequiredMixin, ListView):
    model               = ApplicationFormModel
    template_name       = 'components/list/index.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['token_view'] = 'applicant'
        return super(ApplicationListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.filter(type = 'apply_now')

@method_decorator(is_unauthenticated, name = 'dispatch')
class ContactListView(LoginRequiredMixin, ListView):
    model               = ApplicationFormModel
    template_name       = 'components/list/index.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['token_view'] = 'contact us'
        return super(ContactListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.filter(type = 'contact_us')

class MediaListView(LoginRequiredMixin, ListView):
    model               = MediaModel
    template_name       = 'components/list/index.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['token_view'] = 'media'
        kwargs['slug'] = self.kwargs.get('slug')
        kwargs['token'] = self.kwargs.get('token')
        return super(MediaListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        if self.kwargs.get('slug') == 'department':
            return self.model.objects.filter(media_token_department = self.kwargs.get('token_id'))
        elif self.kwargs.get('slug') == 'jobposition':
            return self.model.objects.filter(media_token_jobposition = self.kwargs.get('token_id'))
        elif self.kwargs.get('slug') == 'application':
            return self.model.objects.filter(media_token_application = self.kwargs.get('token_id'))
        return self.model.objects.filter(media_token_web_contents = self.kwargs.get('token_id'))

# CREATE VIEWS

@method_decorator(is_unauthenticated, name = 'dispatch')
class NewsEventsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'components/create/index.html'
    form_class    = NewsEventsForm

    def get_context_data(self, **kwargs):
        kwargs['form_title'] = 'News &amp; Events'
        return super(NewsEventsCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Successfully created.')
        self.object = form.save()
        return super(NewsEventsCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(NewsEventsCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('apps:createnewsevents')

@method_decorator(is_unauthenticated, name = 'dispatch')
class DepartmentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'components/create/index.html'
    form_class    = DepartmentForm

    def get_context_data(self, **kwargs):
        kwargs['form_title'] = 'Department'
        kwargs['is_file_require'] = True
        return super(DepartmentCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Successfully created.')
        self.object = form.save()
        return super(DepartmentCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(DepartmentCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('apps:createdepartment')

# UPDATE VIEWS

@method_decorator(is_unauthenticated, name = 'dispatch')
class NewsEventsUpdateView(LoginRequiredMixin, UpdateView):
    model = WebContentModel
    template_name = 'components/create/index.html'
    form_class    = NewsEventsForm

    def get_queryset(self):
        return self.model.objects.filter(pk = self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        kwargs['form_title'] = 'News &amp; Events'
        return super(NewsEventsUpdateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Successfully updated.')
        self.object = form.save()
        return super(NewsEventsUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(NewsEventsUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('apps:createnewsevents')

@method_decorator(is_unauthenticated, name = 'dispatch')
class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = DepartmentModel
    template_name = 'components/create/index.html'
    form_class    = DepartmentForm

    def get_queryset(self):
        return self.model.objects.filter(pk = self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        kwargs['form_title'] = 'Department'
        return super(DepartmentUpdateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Successfully updated.')
        self.object = form.save()
        return super(DepartmentUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(DepartmentUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('apps:createdepartment')

# FORM VIEWS

@method_decorator(is_unauthenticated, name = 'dispatch')
class JobPositionCreateView(LoginRequiredMixin, FormView):
    template_name = 'components/create/index.html'
    form_class    = JobPositionForm

    def get_form_kwargs(self):
        kwargs = super(JobPositionCreateView, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['form_title'] = 'Job Position'
        return super(JobPositionCreateView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, 'Successfully created.')
        self.object = form.save()
        return super(JobPositionCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(JobPositionCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('apps:createjobposition', kwargs = {
            'department_id': self.kwargs.get('department_id')
        })

@method_decorator(is_unauthenticated, name = 'dispatch')
class JobQualificationCreateView(LoginRequiredMixin, CreateView):
    template_name = 'components/create/index.html'
    form_class    = JobQualificationForm

    def get_form_kwargs(self):
        kwargs = super(JobQualificationCreateView, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['form_title'] = 'Qualification'
        return super(JobQualificationCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Successfully created.')
        self.object = form.save()
        return super(JobQualificationCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(JobQualificationCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('apps:createjobqualification', kwargs = {
            'jobposition_id': self.kwargs.get('jobposition_id')
        })

@method_decorator(is_unauthenticated, name = 'dispatch')
class MediaUploadCreateView(LoginRequiredMixin, FormView):
    template_name = 'components/create/index.html'
    form_class    = MediaForm

    def get_context_data(self, **kwargs):
        kwargs['is_file_require'] = True
        return super(MediaUploadCreateView, self).get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super(MediaUploadCreateView, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())
        if form.is_valid():
            fetch_object_token = None

            if self.kwargs.get('slug') == 'web':
                fetch_object_token = WebContentModel.objects.get(media_token = self.request.POST.get('media_token'))
            elif self.kwargs.get('slug') == 'department':
                fetch_object_token = DepartmentModel.objects.get(media_token = self.request.POST.get('media_token'))
            elif self.kwargs.get('slug') == 'jobposition':
                fetch_object_token = JobPositionModel.objects.get(media_token = self.request.POST.get('media_token'))
            elif self.kwargs.get('slug') == 'application':
                fetch_object_token = ApplicationFormModel.objects.get(media_token = self.request.POST.get('media_token'))
            
            if fetch_object_token is not None:
                for files in self.request.FILES.getlist('filename'):
                    media_model = MediaModel()
                    if self.kwargs.get('slug') == 'web':
                        media_model.media_token_web_contents = fetch_object_token
                    elif self.kwargs.get('slug') == 'department':
                        media_model.media_token_department = fetch_object_token
                    elif self.kwargs.get('slug') == 'jobposition':
                        media_model.media_token_jobposition = fetch_object_token
                    elif self.kwargs.get('slug') == 'application':
                        media_model.media_token_application = fetch_object_token
                    media_model.filename = files
                    media_model.save()
            else:
                return self.form_invalid(form)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, 'Media is added to library.')
        return super(MediaUploadCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MediaUploadCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('apps:uploadcontentmedia', kwargs = {
            'slug': self.kwargs.get('slug'),
            'token': self.kwargs.get('token')
        })
        

# DELETE VIEWS

class NewsEventsDeleteView(LoginRequiredMixin, DeleteView):
    model = WebContentModel

    def get_success_url(self):
        return reverse_lazy('apps:listviewmodule', kwargs = {
            'slug': self.kwargs.get('slug')
        })

class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = DepartmentModel

    def get_success_url(self):
        return reverse_lazy('apps:departmentlistview', kwargs = {
            'slug': 'department'
        })

class JobPositionDeleteView(LoginRequiredMixin, DeleteView):
    model = JobPositionModel

    def get_success_url(self):
        return reverse_lazy('apps:jobpositionlistview', kwargs = {
            'slug': self.kwargs.get('slug'),
            'id': self.kwargs.get('id')
        })

class JobQualificationDeleteView(LoginRequiredMixin, DeleteView):
    model = JobQualificationModel

    def get_success_url(self):
        return reverse_lazy('apps:listviewmodule', kwargs = {
            'slug': self.kwargs.get('slug'),
            'id': self.kwargs.get('id')
        })

class MediaDeleteView(LoginRequiredMixin, DeleteView):
    model = MediaModel

    def get_success_url(self):
        return reverse_lazy('apps:medialistview', kwargs = {
            'slug': self.kwargs.get('slug'),
            'token_id': self.kwargs.get('token_id'),
            'token': self.kwargs.get('token')
        })