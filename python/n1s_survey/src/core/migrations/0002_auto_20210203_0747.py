# Generated by Django 3.1.1 on 2021-02-03 07:47

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='control_no',
            field=models.CharField(blank=True, default=core.models.initializeControlNumber, max_length=250, null=True),
        ),
    ]
