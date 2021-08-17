from django.db import models, connection
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework.authtoken.models import Token


# Create your models here.


USER_TYPE_OPTIONS = [
    ('1', 'ADMIN'),
    ('2', 'GTM'),
    ('3', 'SALESPERSON'),
    ('4', 'EXECOM')
]


class Users(AbstractUser):
    link_mcp       = models.CharField(max_length = 200, blank = True, null = True, unique = True, verbose_name = 'link mcp data', error_messages = {'unique': 'Link MCP data is already exists.'})
    user_type      = models.CharField(max_length = 10, default = 2, choices = USER_TYPE_OPTIONS, verbose_name = _('account type'))
    account_status = models.CharField(max_length = 120, default = 'pending')

    @receiver(post_save, sender = settings.AUTH_USER_MODEL, dispatch_uid = 'signal_create_token_group')
    def create_token_group(sender, instance = None, created = False, **kwargs):
        if created:
            Token.objects.create(user = instance)
            if instance.user_type == '1':
                group, group_created = Group.objects.get_or_create(name = 'admin')
                instance.groups.add(group)
            if instance.user_type == '2':
                group, group_created = Group.objects.get_or_create(name = 'gtm')
                instance.groups.add(group)
            elif instance.user_type == '3':
                group, group_created = Group.objects.get_or_create(name = 'sales')
                instance.groups.add(group)
            elif instance.user_type == '4':
                group, group_created = Group.objects.get_or_create(name = 'execom')
                instance.groups.add(group)

    def __str__(self):
        return f'{self.first_name.lower()} {self.last_name.lower()}'

    class Meta:
        db_table = 'users'


class Mcpmasterlist(models.Model):
    cust_code      = models.CharField(max_length = 20, blank = True, null = True)
    customer       = models.CharField(max_length = 250, blank = True, null = True)
    scode          = models.CharField(max_length = 10, blank = True, null = True)
    salesperson    = models.CharField(max_length = 250, blank = True, null = True)
    ave_nps        = models.CharField(max_length = 150, blank = True, null = True)
    class_label    = models.CharField(max_length = 150, blank = True, null = True)
    address        = models.CharField(max_length = 250, blank = True, null = True)
    area           = models.CharField(max_length = 250, blank = True, null = True)
    odd_even       = models.CharField(max_length = 10, blank = True, null = True)
    branch         = models.CharField(max_length = 5, blank = True, null = True)
    channel        = models.CharField(max_length = 10, blank = True, null = True)
    freq           = models.CharField(max_length = 5, blank = True, null = True)
    day            = models.CharField(max_length = 10, blank = True, null = True)
    cterm          = models.CharField(max_length = 150, blank = True, null = True)
    climit         = models.CharField(max_length = 150, blank = True, null = True)
    sman_type      = models.CharField(max_length = 150, blank = True, null = True)
    gtm            = models.CharField(max_length = 250, blank = True, null = True)
    group          = models.CharField(max_length = 150, blank = True, null = True)
    town           = models.CharField(max_length = 250, blank = True, null = True)
    zip_code       = models.CharField(max_length = 150, blank = True, null = True)
    channel_group  = models.CharField(max_length = 150, blank = True, null = True)
    channel_group2 = models.CharField(max_length = 150, blank = True, null = True)
    chain          = models.CharField(max_length = 250, blank = True, null = True)
    area_class     = models.CharField(max_length = 50, blank = True, null = True)
    old_new        = models.CharField(max_length = 5, blank = True, null = True)
    geolocation    = models.CharField(max_length = 150, blank = True, null = True)

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table};')

    class Meta:
        db_table = 'mcpmasterlist'
