# Generated by Django 3.2.4 on 2021-07-03 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0016_webanalyticsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='webanalyticsmodel',
            name='visit_count',
            field=models.IntegerField(default=0),
        ),
    ]