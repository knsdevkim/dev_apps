from django.shortcuts import render
from django.core.paginator import Paginator

from apps.product.models import ProductModel

def cashier(request):
    context = {}

    products    = Paginator(ProductModel.objects.all().order_by('-pk'), 6)

    if request.method == 'GET':
        if 'search' in request.GET:
            products = Paginator(ProductModel.objects.filter(name__contains = request.GET.get('search')), 6)
            context['queue'] = True
    
    page_number = request.GET.get('page')
    page_obj    = products.get_page(page_number)

    context['products'] = page_obj

    return render(request, 'components/cashier/index.html', context = context)