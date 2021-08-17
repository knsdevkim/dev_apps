from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

import uuid

class MediaModel(models.Model):
    id             = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    content_type   = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id      = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_id')
    file           = models.ImageField(upload_to = 'images/', blank = False, null = False, verbose_name = 'File')

    class Meta:
        db_table = 'tbl_media'
