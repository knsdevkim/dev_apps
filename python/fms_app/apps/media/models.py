from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

import uuid

class CharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(CharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class MediaModel(models.Model):
    id             = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    content_type   = models.ForeignKey(ContentType, blank = True, null = True, on_delete = models.CASCADE)
    object_id      = models.UUIDField(blank = True, null = True)
    content_object = GenericForeignKey('content_type', 'object_id')
    media_file     = models.ImageField(upload_to = 'profiles/', default = '', blank = False, null = False, verbose_name = 'Profile Picture')
    status         = CharField(max_length = 10, default = 'active', blank = False, null = False)
    record_created = models.DateField(auto_now = True)

    def __str__(self):
        return str(self.media_file)

    class Meta:
        db_table = 'tbl_media'

class DocumentModel(models.Model):
    id             = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    content_type   = models.ForeignKey(ContentType, blank = False, null = False, on_delete = models.CASCADE)
    object_id      = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_id')
    document_name  = CharField(max_length = 150, default = '', blank = False, null = False, verbose_name = 'Document Name', help_text = 'Require to provide document name or else the document will not be upload.')
    media_file     = models.FileField(upload_to = 'documents/', default = '', blank = False, null = False, verbose_name = 'Document File')
    record_created = models.DateField(auto_now = True)

    def __str__(self):
        return self.document_name

    class Meta:
        db_table = 'tbl_documents'