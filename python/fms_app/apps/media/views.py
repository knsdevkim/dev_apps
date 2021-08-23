from django.shortcuts import render, redirect, HttpResponse, Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from apps.vehicle.models import VehicleModel
from apps.operator.models import OperatorModel

from .forms import *

import os

# Download

def download(request, file):
    filepath = settings.MEDIA_ROOT / file

    print('file: {}'.format(filepath))

    if os.path.exists(filepath):
        response = HttpResponse(content_type = 'application/force-download')
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(filepath)
        return response
    raise Http404

# Media Upload

def new_media_upload(request, type = None, pk = None):
    
    context = {
        'type': type,
        'object_id': pk,
        'form': MediaForm
    }

    if request.method == 'POST':
        instance_media = MediaForm(request.POST, request.FILES)
        
        if instance_media.is_valid():
            content_object = None

            if request.POST.get('type') == 'operator':
                content_object = OperatorModel.objects.get(pk = request.POST.get('object_id'))
            elif request.POST.get('type') == 'vehicle':
                content_object = VehicleModel.objects.get(pk = request.POST.get('object_id'))

            MediaModel(
                content_object = content_object,
                media_file = request.FILES.get('media_file')
            ).save()
            messages.success(request, _('Profile image has been uploaded.'))
            
            if request.POST.get('type') == 'operator':
                return redirect(reverse('apps:operator:operatorDetail', kwargs = {
                    'pk': request.POST.get('object_id')
                }))
            elif request.POST.get('type') == 'vehicle':
                return redirect(reverse('apps:vehicle:vehicleDetails', kwargs = {
                    'pk': request.POST.get('object_id')
                }))
        else:
            messages.error(request, _('Could not upload your image make sure your file is an image and it is always require to provide when uploading.'))
            
            return redirect(reverse('apps:media:uploadMedia', kwargs = {
                'type': request.POST['type'],
                'pk': request.POST['object_id']
            }))

    return render(request, 'components/uploads/media.html', context = context)

def media_upload(request):

    if request.method == 'POST':
        instance_media = MediaForm(request.POST, request.FILES)
        to_reverse = None

        if request.POST.get('type') == 'operator':
            to_reverse = 'apps:operator:operatorDetail'
        elif request.POST.get('type') == 'vehicle':
            to_reverse = 'apps:vehicle:vehicleDetails'
        
        if instance_media.is_valid():
            content_object = None

            if request.POST.get('type') == 'operator':
                content_object = OperatorModel.objects.get(pk = request.POST.get('object_id'))
            elif request.POST.get('type') == 'vehicle':
                content_object = VehicleModel.objects.get(pk = request.POST.get('object_id'))

            # Check if media has an object then change the status to 'inactive'
            media_collection = MediaModel.objects.filter(content_type = ContentType.objects.get_for_model(content_object), object_id = request.POST.get('object_id'), status = 'active')

            if media_collection != None:
                media_collection.update(status = 'inactive')

            MediaModel(
                content_object = content_object,
                media_file = request.FILES.get('media_file')
            ).save()

            messages.success(request, _('Profile image has been change.'))
        else:
            messages.error(request, _('Could not upload your image make sure your file is an image and it is always require to provide when uploading.'))

    return redirect(reverse(to_reverse, kwargs = {
        'pk': request.POST['object_id']
    }))

def document_upload(request):
    
    if request.method == 'POST':
        instance_document = DocumentForm(request.POST, request.FILES)
        to_reverse = None

        if request.POST.get('type') == 'operator':
            to_reverse = 'apps:operator:operatorDetail'
        elif request.POST.get('type') == 'vehicle':
            to_reverse = 'apps:vehicle:vehicleDetails'

        if instance_document.is_valid():
            content_object = None

            if request.POST.get('type') == 'operator':
                content_object = OperatorModel.objects.get(pk = request.POST.get('object_id'))
            elif request.POST.get('type') == 'vehicle':
                content_object = VehicleModel.objects.get(pk = request.POST.get('object_id'))

            DocumentModel(
                content_object = content_object,
                document_name = request.POST.get('document_name'),
                media_file = request.FILES.get('media_file')
            ).save()

            messages.success(request, _('Document has beend uploaded.'))
        else:
            messages.error(request, _('Could not upload your document file make it sure it is valid and provided to upload.'))
    
    return redirect(reverse(to_reverse, kwargs = {
        'pk': request.POST.get('object_id')
    }))

# Delete Media

class MediaDeleteView(DeleteView):
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