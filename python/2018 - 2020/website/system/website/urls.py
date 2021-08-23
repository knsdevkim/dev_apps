from django.urls import path

from .views import *

app_name = 'website'

urlpatterns = [
    path('', index, name = 'website_index'),
    path('aboutus/', about_us, name = 'website_about_us'),
    path('products/', products, name = 'website_products'),
    path('newsevents/', newsevents, name = 'website_newsevents'),
    path('newsevents/read/article/<int:id>/', newsevents, name = 'website_newsevents_read'),
    path('careers/', careers, name = 'website_careers'),
    path('careers/<str:filter>/<int:id>/', careers, name = 'website_careers_filter'),
    path('contactus/', contact_us, name = 'website_contact_us'),
    path('nestleprofessionals/', nestleprofessional, name = 'website_nestleprofessionals'),

    # BACKEND URL's
    path('apply/<int:job_id>/', apply, name = 'apply'),
]