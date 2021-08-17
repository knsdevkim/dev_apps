from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from apps.media.models import MediaModel
from .models import ProductModel
from .forms import ProductForm

# List

class ProductListView(ListView):
    model               = ProductModel
    template_name       = 'components/product/list.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        kwargs['product_form'] = ProductForm(category_fk = self.kwargs['category'])
        return super(ProductListView, self).get_context_data(**kwargs)

# Create

def new_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_instance = product_form.save()
            MediaModel(
                content_object = ProductModel.objects.get(pk = product_instance.pk),
                file = request.FILES.get('image')
            ).save()
            messages.success(request, _('Product created.'))
        else:
            messages.error(request, _('Could not save product due to some error, Check and try again.'))
            print(product_form.errors)
    return redirect(reverse('apps:product:productlist', kwargs = {
        'category': request.POST.get('category_fk')
    }))