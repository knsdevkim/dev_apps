# Generated by Django 3.2.4 on 2021-06-26 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_applicationformmodel_concern'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcontentmodel',
            name='type',
            field=models.CharField(choices=[('news_and_events', 'NEWS AND EVENTS')], max_length=150),
        ),
    ]