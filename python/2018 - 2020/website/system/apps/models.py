from django.db import models
from django.utils import timezone

import string
import random

# Create your models here.

EMPLOYEE_POSITION_CHOICES = [
        ('Warehouse Picker', 'Warehouse Picker'),
        ("Helper", "Helper"),
        ("Company Driver", "Company Driver"),
        ("SHE Officer", "SHE Officer"),
        ("Salesman", "Salesman"),
        ("Warehouse Coordinator", "Warehouse Coordinator"),
        ("Operations Manager - Nestle Professional", "Operations Manager - Nestle Professional"),
        ("Accounting Assistant - Inventory  ", "Accounting Assistant - Inventory  "),
        ("Maggi Dedicated Seller", "Maggi Dedicated Seller"),
        ("Encoder", "Encoder"),
        ("Company Nurse", "Company Nurse"),
        ("Delivery Driver", "Delivery Driver"),
        ("Micro D Seller", "Micro D Seller"),
        ("Distributor Key Accounts Specialist - SSF", "Distributor Key Accounts Specialist - SSF"),
        ("DKAS Hybrid", "DKAS Hybrid"),
        ("Activations & Merchandising Manager", "Activations & Merchandising Manager"),
        ("Maggi Dedicated Coordinator", "Maggi Dedicated Coordinator"),
        ("Senior Extruck Salesman", "Senior Extruck Salesman"),
        ("Distributor Customer Service Supervisor", "Distributor Customer Service Supervisor"),
        ("Warehouse Picker", "Warehouse Picker"),
        ("Distributor Major Customer Specialist", "Distributor Major Customer Specialist"),
        ("Ex-truck Driver", "Ex-truck Driver"),
        ("Operations Manager", "Operations Manager"),
        ("Warehouse Checker", "Warehouse Checker"),
        ("Human Resources Specialist - CompBen", "Human Resources Specialist - CompBen"),
        ("Forklift Operator", "Forklift Operator"),
        ("Transport Coordinator", "Transport Coordinator"),
        ("Accounting Assistant - Inventory", "Accounting Assistant - Inventory"),
        ("General Trade Manager", "General Trade Manager"),
        ("Warehouse Admin", "Warehouse Admin"),
        ("NP Distributor Sales Representative", "NP Distributor Sales Representative"),
        ("Accounting Assistant - Cashier", "Accounting Assistant - Cashier"),
        ("Accounting Assistant - AR 2", "Accounting Assistant - AR 2"),
        ("Senior Extruck Salesman; DKAS-Hybrid", "Senior Extruck Salesman; DKAS-Hybrid"),
        ("Utility", "Utility"),
        ("Human Resources Manager", "Human Resources Manager"),
        ("Accounting Assistant - Inventory ", "Accounting Assistant - Inventory "),
        ("Accounting Assistant", "Accounting Assistant"),
        ("Accounting Asst- Asset Manage", "Accounting Asst- Asset Manage"),
        ("Messenger", "Messenger"),
        ("Chief Finance Officer", "Chief Finance Officer"),
        ("Micro D Seller ", "Micro D Seller "),
        ("Management Trainee", "Management Trainee"),
        ("Business Development Officer", "Business Development Officer"),
        ("Relief Salesman", "Relief Salesman"),
        ("Field Checker", "Field Checker"),
        ("Internal Auditor", "Internal Auditor"),
        ("Bookkeeper", "Bookkeeper"),
        ("Barrista", "Barrista"),
        ("Accounting & Finance Officer", "Accounting & Finance Officer"),
        ("Sales Support Specialist", "Sales Support Specialist"),
        ("IT Champ", "IT Champ"),
        ("Motorpool Helper", "Motorpool Helper"),
        ("Sales Admin Support", "Sales Admin Support"),
        ("Senior Relief Salesman", "Senior Relief Salesman"),
        ("Accounting Assistant - IDAS", "Accounting Assistant - IDAS"),
        ("HR Specialist - Recruitment", "HR Specialist - Recruitment"),
        ("NP Dedicated OM", "NP Dedicated OM"),
        ("Corporate Management Trainee", "Corporate Management Trainee"),
        ("Accounting Assistant - A/P Clerk (Supplier)", "Accounting Assistant - A/P Clerk (Supplier)"),
        ("CEO", "CEO"),
        ("Accountant", "Accountant"),
        ("Delivery Helper", "Delivery Helper"),
        ("HR- Training & Development Officer", "HR- Training & Development Officer"),
        ("Micro D Coordinator", "Micro D Coordinator"),
        ("Logistics Admin", "Logistics Admin"),
        ("HR Specialist  ", "HR Specialist  "),
        ("Bad Goods Keeper", "Bad Goods Keeper"),
        ("Software Support", "Software Support"),
        ("NP Business Development Officer", "NP Business Development Officer"),
        ("Accounting Assistant - A/R 1", "Accounting Assistant - A/R 1"),
        ("Mechanic", "Mechanic"),
        ("Delivery Driver ", "Delivery Driver "),
        ("IT Specialist", "IT Specialist"),
        ("Supply Chain Manager", "Supply Chain Manager"),
        ("Employee Relations/Executive Assistant", "Employee Relations/Executive Assistant"),
        ("Technical Support", "Technical Support")
    ]

CONCERN_OPTIONS = [
    ('Bantay Serbisyo', 'Bantay Serbisyo'),
    ('Inquiry', 'Inquiry')
]

class WebContentModel(models.Model):

    NE_OPTIONS = [
        ('News', 'News'),
        ('Events', 'Events')
    ]

    TYPE_OPTIONS = [
        ('news_and_events', 'NEWS AND EVENTS'),
    ]

    media_token = models.TextField(blank = False)
    location    = models.TextField(blank = False, verbose_name = 'Location')
    title       = models.CharField(max_length = 155, blank = False, verbose_name = 'Title')
    description = models.TextField(blank = False, verbose_name = 'Description')
    position    = models.CharField(max_length = 255, choices = EMPLOYEE_POSITION_CHOICES, blank = False, verbose_name = 'Position')
    date_posted = models.DateField(default = timezone.now, verbose_name = 'Date Posted')
    author      = models.CharField(max_length = 150, blank = False, verbose_name = 'Author')
    video       = models.FileField(upload_to = 'n1s_videos/', default = 'N/A', blank = True, null = True, verbose_name = 'Video Stream (Optional)')
    site_map    = models.URLField(max_length = 300, blank = True, verbose_name = 'Site URL')
    ne_type     = models.CharField(max_length = 150, choices = NE_OPTIONS, blank = False, null = False, verbose_name = 'Content Type')
    type        = models.CharField(max_length = 150, choices = TYPE_OPTIONS, blank = False)

    def __str__(self):
        return self.media_token

    class Meta:
        db_table = 'tbl_web_contents'

class ApplicationFormModel(models.Model):
    TYPE_OPTIONS = [
        ('contact_us', 'CONTACT US'),
        ('apply_now', 'APPLY NOW'),
    ]

    firstname           = models.CharField(max_length = 150, blank = False)
    lastname            = models.CharField(max_length = 150, blank = False)
    mobile              = models.CharField(max_length = 13, blank = True)
    address             = models.CharField(max_length = 255, blank = True)
    email               = models.EmailField(blank = False)
    position            = models.CharField(max_length = 255, choices = EMPLOYEE_POSITION_CHOICES, blank = False, null = False)
    concern             = models.CharField(max_length = 255, choices = CONCERN_OPTIONS, blank = False, null = False)
    message             = models.TextField(blank = True)
    media_token         = models.TextField(blank = True)
    filename            = models.FileField(upload_to = 'resume/', blank = False, null = False)
    type                = models.CharField(max_length = 20, choices = TYPE_OPTIONS, blank = False)
    date_posted         = models.DateField(auto_now = True)

    def __str__(self):
        return '{firstname}, {lastname}'

    class Meta:
        db_table = 'tbl_application_forms'

class DepartmentModel(models.Model):
    title       = models.CharField(max_length = 255, blank = False, null = False, verbose_name = 'Department')
    icon        = models.ImageField(upload_to = 'dept_icons/', default = 'N/A', blank = False, null = True)
    description = models.TextField(blank = False, null = False, verbose_name = 'Description')

    def __str__(self):
        return self.title.upper()

    class Meta:
        db_table = 'tbl_deparments'

class JobPositionModel(models.Model):
    media_token  = models.TextField(blank = True)
    department   = models.ForeignKey(DepartmentModel, blank = False, null = False, on_delete = models.CASCADE, related_name = 'departments')
    title        = models.CharField(max_length = 255, blank = False, null = False, verbose_name = 'Job Position')
    description  = models.TextField(blank = False, null = True)
    is_available = models.BooleanField(default = False)

    def __str__(self):
        return self.title.upper()

    class Meta:
        db_table = 'tbl_jobposition'

class JobQualificationModel(models.Model):
    CONTENT_TYPE_OPTIONS = [
        ('requirement', 'Responsibilities'),
        ('qualification', 'Qualification')
    ]

    jobposition  = models.ForeignKey(JobPositionModel, blank = False, null = False, on_delete = models.CASCADE, related_name = 'rn_jpositions')
    title        = models.CharField(max_length = 255, blank = False, null = False)
    content_type = models.CharField(max_length = 155, choices = CONTENT_TYPE_OPTIONS, blank = False, null = False)

    class Meta:
        db_table = 'tbl_qualification'

class MediaModel(models.Model):
    media_token_web_contents   = models.ForeignKey(WebContentModel, null = True, on_delete = models.CASCADE, related_name = 'web')
    media_token_jobposition    = models.ForeignKey(JobPositionModel, null = True, on_delete = models.CASCADE, related_name = 'jobposition')
    filename                   = models.FileField(upload_to = 'web/', verbose_name = 'Upload Media')
    date_uploaded              = models.DateField(auto_now = True)

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'tbl_media'

class WebAnalyticsModel(models.Model):
    user_ip      = models.CharField(max_length = 300, blank = False, null = False)
    visit_count  = models.IntegerField(default = 1)
    date_visited = models.DateField(auto_now = True)

    def __str__(self):
        return self.user_ip

    class Meta:
        db_table = 'tbl_web_analytics'