from django.db import models

# Create your models here.

class FolderModel(models.Model):
    RECORD_TYPE_OPTIONS = [
        ('ada', 'AUTOMATIC DEDUCTION ADVICE'),
        ('itequipment', 'IT EQUIPMENT / SFA SELLING TOOLS ASSIGNMENT FORM')
    ]

    folder = models.CharField(max_length = 150, blank = False, null = True, unique = True, error_messages = {'unique': 'Folder name is already exists.'})
    type_record = models.CharField(max_length = 150, choices = RECORD_TYPE_OPTIONS, blank = False, null = True)
    date_record = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.folder

    class Meta:
        db_table = 'folders'
        ordering = ['-date_record']

class AdaModel(models.Model):
    folder = models.ForeignKey(FolderModel, on_delete = models.CASCADE)
    area = models.CharField(max_length = 50, blank = False, null = True)
    fullname = models.CharField(max_length = 150, blank = False, null = True)
    current_user = models.CharField(max_length = 150, blank = False, null = True)
    position = models.CharField(max_length = 150, blank = False, null = True)
    department = models.CharField(max_length = 150, blank = False, null = True)
    min = models.CharField(max_length = 150, blank = False, null = True)
    plan = models.CharField(max_length = 150, blank = False, null = True)
    package = models.CharField(max_length = 150, blank = False, null = True)
    handset = models.CharField(max_length = 150, blank = False, null = True)

    class Meta:
        db_table = 'ada'
        ordering = ['-pk']

class ItEquipmentModel(models.Model):
    folder = models.ForeignKey(FolderModel, on_delete = models.CASCADE)
    location1 = models.CharField(max_length = 150, blank = False, null = True)
    location2 = models.CharField(max_length = 150, blank = False, null = True)
    userfrom = models.CharField(max_length = 150, blank = False, null = True)
    custodian = models.CharField(max_length = 150, blank = False, null = True)
    device = models.CharField(max_length = 150, blank = False, null = True)
    mobile = models.CharField(max_length = 150, blank = False, null = True)
    imei = models.CharField(max_length = 150, blank = False, null = True)
    iccid = models.CharField(max_length = 150, blank = False, null = True)
    accessories = models.CharField(max_length = 150, blank = False, null = True)
    usertype = models.CharField(max_length = 150, blank = False, null = True)
    operation_manager = models.CharField(max_length = 150, blank = False, null = True)
    is_claim = models.BooleanField(default = False)

    class Meta:
        db_table = 'itequipment'
        ordering = ['-pk']