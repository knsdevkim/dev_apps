# Generated by Django 3.1.1 on 2020-11-03 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201103_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelogsmodel',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
