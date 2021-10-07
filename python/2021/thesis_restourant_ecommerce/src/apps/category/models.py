from django.db import models

import uuid

class CharField(models.CharField):

    def __init__(self, *args, **kwargs):
        super(CharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class CategoryModel(models.Model):
    id           = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name         = CharField(max_length = 15, default = '', blank = False, null = False, unique = True, verbose_name = 'Category Name', error_messages = {'unique': 'Category name is already exists.'})
    date_created = models.DateField(auto_now = True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'tbl_category'
