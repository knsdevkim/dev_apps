from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

AUTHORITY_LEVEL = [
    (2, 'ADMIN'),
    (3, 'TABLET / MOBILE USER')
]

GENDER_OPTIONS = [
    ('Male', 'MALE'),
    ('Femail', 'FEMALE')
]

class Users(AbstractUser):
    auth_level    = models.SmallIntegerField(choices = AUTHORITY_LEVEL, default = 2)
    address       = models.TextField()
    employee_code = models.CharField(max_length = 10, unique = True, error_messages = {
        'unique': 'Employee code is already in use.'
    })
    gender        = models.CharField(max_length = 7, choices = GENDER_OPTIONS)

    @receiver(post_save, sender = settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance = None, created = False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}' if self.first_name != '' else self.username

    class Meta:
        db_table = 'users'


class Racklocation(models.Model):
    rack     = models.IntegerField()
    location = models.IntegerField()
    column   = models.IntegerField()

    def __str__(self):
        return f'R{self.rack}L{self.location}C{self.column}'

    class Meta:
        db_table = 'racklocation'


class Folder(models.Model):
    foldername = models.CharField(max_length = 150, unique = True)
    datetime   = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.foldername

    class Meta:
        db_table = 'folder'


class Products(models.Model):
    folder          = models.ForeignKey(Folder, on_delete = models.CASCADE)
    racklocation    = models.ManyToManyField(Racklocation)
    stockcode       = models.CharField(max_length = 50)
    description     = models.TextField()
    case            = models.IntegerField()
    inner_box       = models.IntegerField()
    piece           = models.IntegerField()
    inventory_value = models.DecimalField(max_digits = 12, decimal_places = 2)
    batch_code      = models.CharField(max_length = 30)
    expiry_date     = models.DateField()
    
    def __str__(self):
        return f'{self.stockcode} - {self.description}'

    class Meta:
        db_table = 'products'


class Validation(models.Model):
    reconcile_stockcode   = models.CharField(max_length = 150)
    reconcile_description = models.TextField()
    qty                   = models.IntegerField()
    expiry_date           = models.DateField()

    class Meta:
        db_table = 'product_validation'
