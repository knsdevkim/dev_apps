from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

from apps.forms import ApplicationForm, ContactForm


from django.core.paginator import Paginator
from django.db.models import Q

from datetime import datetime

from apps.models import WebContentModel, DepartmentModel, JobPositionModel, WebAnalyticsModel, ApplicationFormModel

# Create your views here.

def index(request):
    user_ip = request.META.get('HTTP_FORWARDED_FOR')

    request.session['isInfoNeedToShow'] = True

    if "counter_info_show" not in request.session.keys():
        request.session['counter_info_show'] = 0
        request.session['counter_info_show'] += 1
        request.session.modified
    elif request.session['counter_info_show'] <= 1:
        request.session['counter_info_show'] = 0
        request.session['isInfoNeedToShow'] = False
        request.session.modified

    if user_ip:
        user_ip = request.META.get('HTTP_FORWARDED_FOR').split(', ')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')

    data, create = WebAnalyticsModel.objects.get_or_create(date_visited = datetime.now(), user_ip = user_ip)

    if create == False:
        data.visit_count = data.visit_count + 1
        data.save()

    context = {}
    return render(request, 'website_components/pages/index.html', context = context)

def about_us(request):
    context = {}
    return render(request, 'website_components/pages/about.html', context = context)

def products(request):
    context = {}
    return render(request, 'website_components/pages/products.html', context = context)

def newsevents(request, id = None):
    newsevents_list = WebContentModel.objects.prefetch_related('web').filter(type = 'news_and_events').order_by('-date_posted')
    paginator       = Paginator(newsevents_list, 3)

    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)

    upcoming_events = WebContentModel.objects.all().first()

    if request.method == 'POST':
        queue_result = WebContentModel.objects.prefetch_related('web').filter(title = request.POST.get('search'), type = 'news_and_events')
        return render(request, 'website_components/pages/newsevents.html', context = {'page_obj': queue_result, 
        'count_result': queue_result.count(), 
        'upcoming_events': upcoming_events, 
        'isFilter': True, 
        'queue': request.POST.get('search')})

    if id == None:
        return render(request, 'website_components/pages/newsevents.html', context = {'page_obj': page_obj, 'upcoming_events': upcoming_events})
    else:
        data = WebContentModel.objects.prefetch_related('web').filter(pk = id)
        other_articles = WebContentModel.objects.prefetch_related('web').filter(~Q(pk = id))
        return render(request, 
        'website_components/pages/newseventsread.html', 
        context = {'articles': data, 'other_articles': other_articles})

def careers(request, id = None, filter = None):
    form = ApplicationForm

    isApplicationActive = False

    if request.method == 'POST':
        objects = ApplicationForm(request.POST, request.FILES)
        if objects.is_valid():
            save_data = objects.save()

            # After object saved, forward the data to the perspective email.

            message = f"""
            Online Applicant Name: {save_data.lastname}, {save_data.firstname}
            Email: {save_data.email}
            Tel. No.: {save_data.mobile}
            Applying For: {save_data.position}

            Applicant Message:
            {save_data.message}
            """
            
            email = EmailMessage('No. 1 Supplier, Inc. - Website Application Form', 
            message, 
            settings.EMAIL_HOST_USER, 
            ['n1s.jobposting@gmail.com'])

            email.attach_file(f'{settings.BASE_DIR}/media/{save_data.filename}')
            
            email.send()
            
            isApplicationActive = True
        else:
            return render(request, 'website_components/pages/careers.html', context = {'form': objects})


    if id == None:
        return render(request, 'website_components/pages/careers.html', context = {
            'form': form, 
            'departments_object': DepartmentModel.objects.all(),
            'isApplicationActive': isApplicationActive})
    elif filter != None and filter == 'jobs':
        return render(request, 'website_components/pages/careersfilter.html', context = {'id': id, 'department': DepartmentModel.objects.prefetch_related('departments').get(pk = id)})
    elif filter != None and filter == 'position':
        return render(request, 'website_components/pages/careersread.html', context = {
            'data': JobPositionModel.objects.prefetch_related('jobposition').prefetch_related('rn_jpositions').get(pk = id),
            'id': id
            })


def contact_us(request):
    form = ContactForm

    isApplicationActive = False

    if request.method == 'POST':
        objects = ContactForm(request.POST)
        if objects.is_valid():
            save_data = objects.save()

            # After object saved, forward the data to the perspective email.

            message = f"""
            Concern From: {save_data.lastname}, {save_data.firstname}
            Email: {save_data.email}
            Concern Category: {save_data.concern}

            Message:
            {save_data.message}
            """

            email = EmailMessage('No. 1 Supplier, Inc. - Contact Us Concerns', 
            message, 
            settings.EMAIL_HOST_USER, 
            ['n1s.pscabantug@gmail.com'])
            email.send()

            isApplicationActive = True

        else:
            return render(request, 'website_components/pages/contact_us.html', context = {'form': objects})

    return render(request, 'website_components/pages/contact_us.html', context = {
        'form': form,
        'isApplicationActive': isApplicationActive
        })

def nestleprofessional(request):
    return render(request, 'website_components/pages/nestle_professionals.html', context = {})

# Application
def apply(request, job_id = None):

    if request.method == 'POST':
        data = request.POST
        
        save_data = ApplicationFormModel.objects.create(
            type = 'apply_now',
            firstname = data.get('firstname'),
            lastname = data.get('lastname'),
            position = data.get('position'),
            email = data.get('email'),
            mobile = data.get('mobile'),
            message = data.get('message'),
            filename = request.FILES["filename"]
        )

        message = f"""
        Online Applicant Name: {save_data.lastname}, {save_data.firstname}
        Email: {save_data.email}
        Tel. No.: {save_data.mobile}
        Applying For: {save_data.position}

        Applicant Message:
        {save_data.message}
        """
        
        email = EmailMessage('No. 1 Supplier, Inc. - Website Application Form', 
        message, 
        settings.EMAIL_HOST_USER, 
        ['n1s.jobposting@gmail.com'])

        email.attach_file(f'{settings.BASE_DIR}/media/{save_data.filename}')
        
        email.send()

        messages.success(request, 'Application submitted successfully!')

    return redirect(reverse('website:website_careers_filter', kwargs = {
        'filter': 'position',
        'id': job_id
    }))