from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DeleteView

from .forms import *

from apps.category.models import CategoryModel
from .models import ProductModel

# List

class ProductListView(ListView):
    paginate_by         = 25
    model               = ProductModel
    template_name       = 'components/product/list.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        kwargs['page_name']      = 'Products'
        kwargs['sub_page_name'] = self.kwargs['category']
        kwargs['product_form']  = ProductForm
        kwargs['fk'] = get_object_or_404(CategoryModel, name = self.kwargs['category']).pk
        return super(ProductListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.filter(fk__name = self.kwargs['category'])

# Create

def new_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, _('Product has been added.'))
        else:
            print(product_form.errors)
            messages.error(request, _('Could not save product, Try again.'))
    return redirect(reverse('apps:product:productList', kwargs = {
        'category': get_object_or_404(CategoryModel, pk = request.POST.get('fk')).name
    }))

# Delete

class ProductDeleteView(DeleteView):
    model = ProductModel

    def get_success_url(self):
        messages.success(self.request, _('Product deleted.'))
        return reverse_lazy('apps:product:productList', kwargs = {
            'category': self.kwargs['category']
        })