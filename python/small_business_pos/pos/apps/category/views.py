from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from .forms import CategoryForm

from .models import CategoryModel

# Category List

class CategoryListView(ListView):
    paginate_by         = 20
    model               = CategoryModel
    template_name       = 'components/category/list.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        kwargs['page_name']     = 'Product Category'
        kwargs['category_form'] = CategoryForm()
        return super(CategoryListView, self).get_context_data(**kwargs)

# Category create

def new_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, _('New category has been save.'))
        else:
            messages.error(request, _('Could not save new category.'))
    return redirect(reverse('apps:category:categoryList'))

# Delete

# Delete

class CategoryDeleteView(DeleteView):
    model = CategoryModel

    def get_success_url(self):
        messages.success(self.request, _('Category deleted.'))
        return reverse_lazy('apps:category:categoryList')