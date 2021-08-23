from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Prefetch, Count, Sum
from django.utils.translation import gettext_lazy as _

from datetime import datetime

from .models import VEHICLE_TYPE_OPTIONS, VehicleModel, VehicleCrModel, VehicleOrModel, VehicleOrBreakdownPaymentModel
from apps.media.forms import MediaForm, DocumentForm
from .forms import *

# FUNCTIONS

# Get ownership object of the vehicle
def vehicle_ownership():
    return VehicleModel.objects.all().values('ownership').annotate(n_ownership = Count('ownership'))

# Vehicle types
def vehicle_types():
    return [set(_) for _ in VEHICLE_TYPE_OPTIONS]

# Vehicle List

class VehicleListView(ListView):
    paginate_by         = 15
    model               = VehicleModel
    template_name       = 'components/vehicle/list.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        # For filtering search
        kwargs['vehicle_ownership'] = vehicle_ownership
        kwargs['vehicle_type']      = vehicle_types

        kwargs['total_data'] = self.get_queryset().count()
        return super(VehicleListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.prefetch_related('fk_cr_rn').prefetch_related('media').all()

# Vehicle Details

class VehicleDetailView(DetailView):
    model               = VehicleModel
    pk_url_kwarg        = 'pk'
    template_name       = 'components/vehicle/details.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        kwargs['or_form']       = VehicleCreateOrForm
        kwargs['pk']            = self.kwargs[self.pk_url_kwarg]
        kwargs['media_form']    = MediaForm
        kwargs['document_form'] = DocumentForm
        return super(VehicleDetailView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.prefetch_related('fk_cr_rn').prefetch_related('fk_or_rn').prefetch_related('media').filter(pk = self.kwargs[self.pk_url_kwarg]) 

# Vehicle Print

class VehiclePrintView(DetailView):
    context_object_name = 'data'

    def get_queryset(self):
        if self.kwargs['print_for'] == 'or':
            return VehicleOrModel.objects.prefetch_related('fk_orbp_rn').filter(pk = self.kwargs[self.pk_url_kwarg]).annotate(grand_total = (Sum('fk_orbp_rn__qty') * Sum('fk_orbp_rn__cost')))
        elif self.kwargs['print_for'] == 'cr':
            return VehicleCrModel.objects.filter(pk = self.kwargs[self.pk_url_kwarg])
        elif self.kwargs['print_for'] == 'detail':
            return VehicleModel.objects.filter(pk = self.kwargs[self.pk_url_kwarg])

    def get_template_names(self):
        if self.kwargs['print_for'] == 'or':
            self.template_name = 'components/vehicle/prints/or/index.html'
            return self.template_name
        elif self.kwargs['print_for'] == 'cr':
            self.template_name = 'components/vehicle/prints/cr/index.html'
            return self.template_name
        elif self.kwargs['print_for'] == 'detail':
            self.template_name = 'components/vehicle/prints/detail/index.html'
            return self.template_name

# Vehicle Search

def vehicle_search(request):
    
    context = {}
    
    if request.method == 'GET':
        if 'q' in request.GET:
            # Look for the object of main model if provided
            # the prefetch_related will look for the object filter by the frontend
            # and include to the query if provided.
            vehicle_list = VehicleModel.objects.prefetch_related(
                Prefetch(
                    'fk_cr_rn',
                    queryset = VehicleCrModel.objects.filter(
                          Q(plate_no__iexact = request.GET.get('plate_no')) 
                        | Q(mvfile_no__icontains = request.GET.get('file_no'))
                        | Q(cr_no__icontains = request.GET.get('cr_no')) 
                    )
                )
            ).prefetch_related(
                Prefetch(
                    'fk_or_rn',
                    queryset = VehicleOrModel.objects.filter(
                        Q(or_no__icontains = request.GET.get('or_no'))
                    )
                )
            ).filter(
               ((Q(vehicle_name__iexact = request.GET.get('q'))
             | Q(area_coverage__iexact = request.GET.get('q')))) 
             | (Q(case_capacity__icontains = request.GET.get('case_capacity')) 
             & Q(ownership__icontains = request.GET.get('ownership')) 
             & Q(vehicle_type__exact = request.GET.get('vehicle_type'))))

            total_data   = vehicle_list.count()
            paginator    = Paginator(vehicle_list, 15)

            page_number = request.GET.get('page')
            page_obj    = paginator.get_page(page_number)

            context['vehicle_ownership'] = vehicle_ownership
            context['vehicle_type']      = vehicle_types
            context['total_data']        = total_data
            context['data']              = page_obj

        else:
            messages.error(request, _('You leave empty the field that you are trying to search.'))
            return redirect(reverse('apps:vehicle:vehicleList'))

    return render(request, 'components/vehicle/list.html', context = context)

# Create Vehicle

class VehicleCreateView(CreateView):
    template_name = 'components/vehicle/create.html'

    def get_form_kwargs(self):
        kwargs = super(VehicleCreateView, self).get_form_kwargs()
        if self.kwargs['new_for'] == 'cr':
            kwargs.update({
                'fk': self.kwargs['fk']
            })
            return kwargs
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['new_for'] = self.kwargs['new_for']
        if self.kwargs['new_for'] == 'cr':
            kwargs['fk'] = self.kwargs['fk']
        return super(VehicleCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        if self.kwargs['new_for'] == 'details':
            messages.success(self.request, _('Vehicle details has been saved.'))
        elif self.kwargs['new_for'] == 'cr':
            messages.success(self.request, _('Cr has been added to the vehicle details.'))
        return super(VehicleCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, _('Could not save record due to some error exists, Check and try again.'))
        return super(VehicleCreateView, self).form_invalid(form)

    def get_form_class(self):
        if self.kwargs['new_for'] == 'details':
            self.form_class = VehicleForm
        elif self.kwargs['new_for'] == 'cr':
            self.form_class = VehicleCrForm
        return self.form_class

    def get_success_url(self):
        if self.kwargs['new_for'] == 'details':
            return reverse_lazy('apps:media:uploadMedia', kwargs = {
                'type': 'vehicle',
                'pk': self.object.pk
            })
        elif self.kwargs['new_for'] == 'cr':
            return reverse_lazy('apps:vehicle:vehicleDetails', kwargs = {
                'pk': self.kwargs['fk']
            })

# Create Vehicle Or Details

def create_vehicle_or(request):
    or_form = VehicleCreateOrForm

    if request.method == 'POST':
        or_form_post = VehicleCreateOrForm(request.POST)

        if or_form_post.is_valid():
            fetch_id = or_form_post.save()
            messages.success(request, _('Successfully created new vehicle OR, add some more details ...'))
            return redirect(reverse('apps:vehicle:vehicleOrDetailsCreateUpdate', kwargs = {
                'pk': fetch_id.pk
            }))
        else:
            messages.error(request, _('Could not save vehicle OR due to some errors occured (Duplicate OR No. / Some fields error while saving).'))
            return redirect(reverse('apps:vehicle:vehicleDetails', kwargs = {
                'pk': request.POST.get('fk')
            }))
    return render(request, '404.html', context = {})

# Create / Update Or Vehicle Details and Breakdown payment

def create_update_vehicle_or(request, pk = None):
    fetched_data = VehicleOrModel.objects.prefetch_related('fk_orbp_rn').get(pk = pk)
    obj          = get_object_or_404(VehicleOrModel, pk = pk)
    or_form      = VehicleDetailsUpdateOrForm(instance = obj)
    
    context = {
        'data': fetched_data,
        'or_form': or_form
    }

    if request.method == 'POST':
        form = VehicleDetailsUpdateOrForm(request.POST, instance = obj)
        if form.is_valid():
            instance_or = form.save()
            if 'bp_description' in request.POST:
                for key, description in enumerate(request.POST.getlist('bp_description')):
                    qty  = request.POST.getlist('bp_qty')
                    cost = request.POST.getlist('bp_cost') 
                    if description != '' and qty[key] != '' and cost[key] != '':
                        VehicleOrBreakdownPaymentModel(
                            fk = get_object_or_404(VehicleOrModel, pk = instance_or.pk),
                            description = description,
                            qty = qty[key],
                            cost = cost[key]
                        ).save()
                    else:
                        messages.warning(request, _('There are some fields that are missing in breakdown payment to fill which is not save.'))

            messages.success(request, _('OR has been updated.'))

            return redirect(reverse('apps:vehicle:vehicleOrDetailsCreateUpdate', kwargs = {
                'pk': pk
            }))
        else:
            messages.error(request, _('Could not save record due to some error occured, Try again.'))

    return render(request, 'components/vehicle/or/details/create_update.html', context = context)

# Update Vehicle

class VehicleUpdateView(UpdateView):
    pk_url_kwarg        = 'pk'
    template_name       = 'components/vehicle/edit.html'
    context_object_name = 'data'
    to_modify           = None

    def get_context_data(self, **kwargs):
        if self.to_modify != None:
            kwargs['context_update'] = self.to_modify
            if 'fk' in self.kwargs:
                kwargs['deliver_address'] = self.kwargs.get('fk')
            else:
                kwargs['deliver_address'] = self.kwargs[self.pk_url_kwarg]
        else:
            raise Exception('(to_modify) variable must not be null, and must not be None.')
        return super(VehicleUpdateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, _('Vehicle record has been modified.'))
        return super(VehicleUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Could not modify record, Check fields error message and try again.'))
        return super(VehicleUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('apps:vehicle:vehicleDetails', kwargs = {
            'pk': self.kwargs.get('fk') if 'fk' in self.kwargs else self.kwargs[self.pk_url_kwarg]
        })

# Update Multiple vehicle status

def update_vehicle_status(request):
    if request.method == 'POST':
        if len(request.POST.getlist('object_id')) <= 0:
            messages.error(request, _('No selected data to update.'))
        elif request.POST.get('status') == '':
            messages.error(request, _('No status to change.'))
        else:
            VehicleModel.objects.filter(pk__in = request.POST.getlist('object_id')).update(status = request.POST.get('status'))
            messages.success(request, _('Vehicles status updated.'))
    return redirect(reverse('apps:vehicle:vehicleList'))

# Delete Vehicle

class VehicleDeleteView(DeleteView):
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
