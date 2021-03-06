# Generated by Django 3.2.4 on 2021-07-06 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0017_webanalyticsmodel_visit_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformmodel',
            name='date_posted',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='jobqualificationmodel',
            name='content_type',
            field=models.CharField(choices=[('requirement', 'Responsibilities'), ('qualification', 'Qualification')], max_length=155),
        ),
    ]
