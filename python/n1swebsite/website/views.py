from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from backend.models import *
from backend.forms import *

# Create your views here.

class WebsiteView(TemplateView):
    template_name = 'base/website.html'

    # Set context model to access in template
    def get_context_data(self, **kwargs):
        kwargs['is_maintenance'] = SiteSettingsModel.objects.get(id = 1)

        kwargs['latest_about'] = AboutModel.objects.latest('pk')
        kwargs['latest_branch'] = BranchModel.objects.latest('pk')
        kwargs['latest_newsevent'] = NewsEventModel.objects.latest('pk')

        kwargs['context_object_slideshow'] = SlideshowModel.objects.all()
        kwargs['context_object_about'] = AboutModel.objects.get(id = 1)
        kwargs['context_object_branch'] = BranchModel.objects.all()
        kwargs['context_object_milestone'] = MilestoneModel.objects.all()
        kwargs['context_object_newsevent'] = NewsEventModel.objects.all()
        kwargs['context_object_video'] = VideoModel.objects.all()
        kwargs['context_object_careers'] = CareersModel.objects.all()

        return super().get_context_data(**kwargs)

class SingleView(TemplateView):
    template_name = 'base/singleview.html'

    # Set context model to access in template
    def get_context_data(self, **kwargs):
        kwargs['is_maintenance'] = SiteSettingsModel.objects.get(id = 1)
        kwargs['path'] = self.kwargs['pathfind']
        kwargs['careers'] = CareersModel.objects.all()
        
        kwargs['latest_about'] = AboutModel.objects.latest('pk')
        kwargs['latest_branch'] = BranchModel.objects.latest('pk')
        kwargs['latest_newsevent'] = NewsEventModel.objects.latest('pk')

        if self.kwargs['pathfind'] == 'branch':
            kwargs['context_title'] = 'Branch'
            kwargs['related'] = BranchModel.objects.filter(~Q(pk = self.kwargs['pk']))
            kwargs['object'] = BranchModel.objects.get(id = self.kwargs['pk'])
        elif self.kwargs['pathfind'] == 'milestone':
            kwargs['context_title'] = 'Milestone'
            kwargs['object'] = MilestoneModel.objects.get(id = self.kwargs['pk'])
        elif self.kwargs['pathfind'] == 'newsevent':
            kwargs['context_title'] = 'News &amp; Event'
            kwargs['related'] = NewsEventModel.objects.filter(~Q(pk = self.kwargs['pk']))
            kwargs['object'] = NewsEventModel.objects.get(id = self.kwargs['pk'])
        elif self.kwargs['pathfind'] == 'video':
            kwargs['context_title'] = 'watch'
            kwargs['related'] = VideoModel.objects.filter(~Q(pk = self.kwargs['pk']))
            kwargs['object'] = VideoModel.objects.get(id = self.kwargs['pk'])
        elif self.kwargs['pathfind'] == 'ourstory':
            kwargs['context_title'] = 'our story'
            kwargs['object'] = AboutModel.objects.get(Q(pk = self.kwargs['pk']))
        elif self.kwargs['pathfind'] == 'careers':
            kwargs['context_title'] = 'Careers'
            kwargs['object'] = CareersModel.objects.get(Q(pk = self.kwargs['pk']))  
        return super().get_context_data(**kwargs)

'''
    @class: ContactView
        -> template for contact form.
'''
class ContactView(FormView):
    template_name = 'components/contactus/view.html'
    form_class = ContactusForm

    def get_context_data(self, **kwargs):
        kwargs['latest_about'] = AboutModel.objects.latest('pk')
        kwargs['latest_branch'] = BranchModel.objects.latest('pk')
        kwargs['latest_newsevent'] = NewsEventModel.objects.latest('pk')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Thank you for having some quality time to contact us, Until next time.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Form is not valid to process. Try again.')
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('website:contactus')

class ProductsView(TemplateView):
    template_name = 'components/products/view.html'

    def get_context_data(self, **kwargs):
        kwargs['latest_about'] = AboutModel.objects.latest('pk')
        kwargs['latest_branch'] = BranchModel.objects.latest('pk')
        kwargs['latest_newsevent'] = NewsEventModel.objects.latest('pk')
        return super().get_context_data(**kwargs)

class CareersView(TemplateView):
    template_name = 'components/careers/view.html'

    def get_context_data(self, **kwargs):
        kwargs['context_object_careers'] = CareersModel.objects.all()
        kwargs['latest_about'] = AboutModel.objects.latest('pk')
        kwargs['latest_branch'] = BranchModel.objects.latest('pk')
        kwargs['latest_newsevent'] = NewsEventModel.objects.latest('pk')
        return super().get_context_data(**kwargs)