from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from .models import OperatorModel

from apps.media.forms import MediaForm, DocumentForm
from apps.media.models import MediaModel

from .forms import *

# Operator List

class OperatorListView(ListView):
    paginate_by         = 15
    model               = OperatorModel
    template_name       = 'components/operator/list.html'
    context_object_name = 'data'

    def get_context_data(self, *args, **kwargs):
        kwargs['total_operator_driver'] = self.model.objects.filter(operator_type = 'driver').count()
        kwargs['total_operator_helper'] = self.model.objects.filter(operator_type = 'helper').count()
        return super(OperatorListView, self).get_context_data(*args, **kwargs)

    def get_queryset(self):
        return self.model.objects.prefetch_related('media').all()

# Operator Details

class OperatorDetailView(DetailView):
    model = OperatorModel
    template_name = 'components/operator/details.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        kwargs['pk']            = self.kwargs[self.pk_url_kwarg]
        kwargs['media_form']    = MediaForm
        kwargs['document_form'] = DocumentForm
        return super(OperatorDetailView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.prefetch_related('fk_dl_rn').prefetch_related('media').prefetch_related('document').filter(pk = self.kwargs[self.pk_url_kwarg])

# Operator Search & filter

def operator_search(request):
    context = {}

    if request.method == 'GET':
        if 'q' in request.GET and request.GET.get('q') != '':
            operator_list = OperatorModel.objects.filter(
                (Q(employee_id__iexact = request.GET.get('q')) 
               | Q(firstname__icontains = request.GET.get('q'))
               | Q(lastname__icontains = request.GET.get('q')) 
               | Q(middlename__icontains = request.GET.get('q')) 
               | Q(area__icontains = request.GET.get('q'))) 
               & Q(operator_type__exact = request.GET.get('search_type')))

            paginator   = Paginator(operator_list, 15)
            page_number = request.GET.get('page')
            page_obj    = paginator.get_page(page_number)

            context['data']                  = page_obj

        else:
            messages.error(request, _('You leave empty the field that you are trying to search.'))
            return redirect(reverse('apps:operator:operatorList'))

    return render(request, 'components/operator/search.html', context = context)

# Operator Create

def new_operator(request):
    context = {
        'operatorForm': OperatorDetailsForm,
        'contactForm': ContactForm,
        'licenseForm': DriverLicenseForm
    }

    if request.method == 'POST':
        obj_operator = OperatorDetailsForm(request.POST)
        obj_contact  = ContactForm(request.POST)
        obj_license  = DriverLicenseForm(request.POST)

        if obj_operator.is_valid() and obj_contact.is_valid() and obj_license.is_valid():
            instance_operator = obj_operator.save()
            
            instance_contact = obj_contact.save(commit = False)
            instance_contact.fk = instance_operator
            instance_contact.save()

            instance_license = obj_license.save(commit = False)
            instance_license.fk = instance_operator
            instance_license.save()

            messages.success(request, _('New record has been saved!'))

            return redirect(reverse('apps:media:uploadMedia', kwargs = {
                'type': 'operator',
                'pk': instance_operator.pk
            }))
        else:
            context = {
                'operatorForm': obj_operator,
                'contactForm': obj_contact,
                'licenseForm': obj_license
            }
            messages.error(request, _('Could not save record due to some error occured, Please check and try again.'))
            return render(request, 'components/operator/create.html', context = context)

    return render(request, 'components/operator/create.html', context = context)

# Operator Update

def update_operator(request, pk = None):
    context = {}

    context['data']         = get_object_or_404(OperatorModel, pk = pk)
    context['operatorForm'] = OperatorDetailsForm(instance = get_object_or_404(OperatorModel, pk = pk))
    context['contactForm']  = ContactForm(instance = get_object_or_404(ContactModel, fk = pk))
    context['licenseForm']  = DriverLicenseForm(instance = get_object_or_404(DriverLicenseModel, fk = pk))

    if request.method == 'POST':
        obj_operatorForm = OperatorDetailsForm(request.POST, instance = get_object_or_404(OperatorModel, pk = pk))
        obj_contactForm  = ContactForm(request.POST, instance = get_object_or_404(ContactModel, fk = pk))
        obj_licenseForm  = DriverLicenseForm(request.POST, instance = get_object_or_404(DriverLicenseModel, fk = pk))

        if obj_operatorForm.is_valid() and obj_contactForm.is_valid() and obj_licenseForm.is_valid():
            operator = obj_operatorForm.save()
            
            cf = obj_contactForm.save(commit = False)
            cf.fk = operator
            cf.save()

            lf = obj_licenseForm.save(commit = False)
            lf.fk = operator
            lf.save()

            messages.success(request, _('Record has been updated.'))

            return redirect(reverse('apps:operator:operatorDetail', kwargs = {
                'pk': pk
            }))
        else:
            
            context['operatorForm'] = obj_operatorForm
            context['contactForm']  = obj_contactForm
            context['licenseForm']  = obj_licenseForm

            messages.error(request, _('Could not update data due to some error occured, Please check and try again.'))

    return render(request, 'components/operator/edit.html', context = context)


# Operator Delete

class OperatorDeleteView(DeleteView):
    
    model = None
    to_reverse = None
    with_pk = False

    def get_success_url(self):
        url_reverse = None
        messages.success(self.request, _('Record has been permanently deleted.'))
        if self.with_pk == True:
            url_reverse = reverse_lazy(self.to_reverse, kwargs = {
                'pk': self.kwargs['return_pk']
            })
        else:
            url_reverse = reverse_lazy(self.to_reverse)
        return url_reverse