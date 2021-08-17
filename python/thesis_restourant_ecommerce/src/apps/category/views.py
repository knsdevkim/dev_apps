from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from .models import CategoryModel
from .forms import CategoryForm

# List view

class CategoryListView(ListView):
    model               = CategoryModel
    template_name       = 'components/category/list.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        kwargs['category_form'] = CategoryForm
        return super(CategoryListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.all()

# Create view

class CategoryCreateView(CreateView):
    model         = CategoryModel
    form_class    = CategoryForm

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, _('Category successfully created.'))
        return super(CategoryCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Could not create new category due to some errors. Check and try again.'))
        return redirect(reverse_lazy('apps:category:categorylist'))

    def get_success_url(self):
        return reverse_lazy('apps:category:categorylist')
