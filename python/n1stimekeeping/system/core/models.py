from django.db import models


# Create your models here.
class EmployeeRecordModel(models.Model):
    employee = models.CharField(max_length=6, blank=False, null=True, unique=True, error_messages={
        'unique': 'Employee ID is already exists.'
    })
    business_unit = models.CharField(max_length=50, blank=False, null=True)
    first_name = models.CharField(max_length=50, blank=False, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=True)
    middle_name = models.CharField(max_length=50, blank=False, null=True)
    mobile_number = models.IntegerField(blank=False, null=True)
    email_address = models.EmailField(blank=False, null=True)
    employee_position = models.CharField(max_length=50, blank=False, null=True)
    employee_status = models.CharField(max_length=50, blank=False, null=True)
    date_hired = models.CharField(max_length=50, blank=False)
    date_regularized = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.employee

    class Meta:
        db_table = 'employee_records'
        ordering = ['-pk']


class EmployeeInformationModel(models.Model):
    employee = models.OneToOneField(EmployeeRecordModel, on_delete=models.CASCADE)
    civil_status = models.CharField(max_length=50, blank=False, null=True)
    birthdate = models.CharField(max_length=50, blank=False)
    address_1 = models.TextField(blank=False)
    address_2 = models.TextField(blank=False)
    third_party_employer = models.CharField(max_length=50, blank=False, null=True)
    shirt_size = models.CharField(max_length=50, blank=False, null=True)
    active_status = models.CharField(max_length=20, blank=False, null=True)

    def __str__(self):
        return self.employee

    class Meta:
        db_table = 'employee_information'
        ordering = ['-pk']


class TimeKeepingDateModel(models.Model):
    employee = models.ForeignKey(EmployeeRecordModel, to_field='employee', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        db_table = 'time_keeping_date'
        ordering = ['-pk']


class TimeLogsModel(models.Model):
    date = models.ForeignKey(TimeKeepingDateModel, on_delete=models.CASCADE)
    time = models.CharField(max_length=20)
    status = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.time)

    class Meta:
        db_table = 'time_logs'
        ordering = ['-pk']
        get_latest_by = 'pk'
