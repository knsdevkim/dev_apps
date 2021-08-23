from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

import uuid

from datetime import datetime

from apps.media.models import MediaModel, DocumentModel

OPERATOR_TYPE = [
    ('driver', 'Driver'),
    ('helper', 'Helper')
]

class CharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(CharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class OperatorModel(models.Model):
    id             = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    employee_id    = CharField(max_length = 150, default = '', blank = False, null = False, verbose_name = 'Employee ID')
    firstname      = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'Firstname')
    lastname       = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'Lastname')
    middlename     = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'Middle Name')
    birthdate      = models.DateField(default = datetime.now, blank = False, null = False, verbose_name = 'Date of Birth')
    address        = CharField(max_length = 150, default = '', blank = False, null = False, verbose_name = 'Address', help_text = 'No., Street, City / Municipality, Province, Zip Code')
    contact_no     = CharField(max_length = 13, default = '', blank = False, null = False, verbose_name = 'Contact No.')
    email          = models.EmailField(blank = False, default = '', null = False, verbose_name = 'Email Address', help_text = 'Email must be valid and in use.')
    date_employed  = models.DateField(default = datetime.now, blank = False, null = False, verbose_name = 'Date Employed')
    position       = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'Job Title')
    area           = CharField(max_length = 100, default = 'Not Available', blank = False, null = False, verbose_name = 'Area Coverage')
    operator_type  = CharField(max_length = 15, choices = OPERATOR_TYPE, blank = False, null = False, verbose_name = 'Operator Type', help_text = 'For identification purposes.')
    media          = GenericRelation(MediaModel, related_query_name = 'media')
    document       = GenericRelation(DocumentModel, related_query_name = 'document')
    record_created = models.DateField(auto_now = True)

    def __str__(self):
        return f'{self.lastname.upper()}, {self.firstname.upper()} {self.middlename[:1].upper()}.'

    class Meta:
        db_table = 'tbl_operators'

class ContactModel(models.Model):
    id             = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    fk             = models.OneToOneField(OperatorModel, on_delete = models.CASCADE, related_name = 'fk_c_rn')
    fullname       = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'Contact Person (Fullname)')
    address        = CharField(max_length = 150, default = '', blank = False, null = False, verbose_name = 'Address', help_text = 'No., Street, City / Municipality, Province, Zip Code')
    contact_no     = CharField(max_length = 14, default = '', blank = False, null = False, verbose_name = 'Contact No.')
    relation       = CharField(max_length = 50, default = '', blank = False, null = False, verbose_name = 'Relationship')
    record_created = models.DateField(auto_now = True)

    class Meta:
        db_table = 'tbl_contact'

class DriverLicenseModel(models.Model):
    id              = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    fk              = models.OneToOneField(OperatorModel, on_delete = models.CASCADE, related_name = 'fk_dl_rn')
    license_no      = CharField(max_length = 120, default = 'Not Available', blank = False, null = False, verbose_name = 'License No.')
    expiration_date = models.DateField(default = datetime.now, blank = False, null = False, verbose_name = 'Expiration Date')
    agency_code     = CharField(max_length = 90, default = 'Not Available', blank = False, null = False, verbose_name = 'Agency Code')
    restriction     = CharField(max_length = 15, default = 'Not Available', blank = False, null = False, verbose_name = 'Restriction')
    record_created  = models.DateField(auto_now = True)

    def __str__(self):
        return f'({self.license_no} - {self.fk})'

    class Meta:
        db_table = 'tbl_driver_license'