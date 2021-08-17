from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

import uuid

from apps.category.models import CategoryModel
from apps.media.models import MediaModel

class CharField(models.CharField):

    def __init__(self, *args, **kwargs):
        super(CharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class ProductModel(models.Model):
    id           = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    category_fk  = models.ForeignKey(CategoryModel, on_delete = models.PROTECT)
    name         = CharField(max_length = 25, default = '', blank = False, null = False, unique = True, verbose_name = 'Product Name', error_messages = {'unique': 'Product name is already exists'})
    price        = models.DecimalField(max_digits = 15, decimal_places = 2, default = 0.00, blank = False, null = False, verbose_name = 'Price')
    media        = GenericRelation(MediaModel)
    date_created = models.DateField(auto_now = True)

    class Meta:
        db_table = 'tbl_product'
