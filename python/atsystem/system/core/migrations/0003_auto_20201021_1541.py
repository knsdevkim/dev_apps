# Generated by Django 3.1.1 on 2020-10-21 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_adamodel_remarks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itequipmentmodel',
            old_name='location',
            new_name='location1',
        ),
        migrations.AddField(
            model_name='itequipmentmodel',
            name='location2',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='itequipmentmodel',
            name='userfrom',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='itequipmentmodel',
            name='usertype',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
