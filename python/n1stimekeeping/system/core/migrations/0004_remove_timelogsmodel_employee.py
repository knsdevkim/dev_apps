# Generated by Django 3.1.1 on 2020-11-02 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_timelogsmodel_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timelogsmodel',
            name='employee',
        ),
    ]