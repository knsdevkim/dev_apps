# Generated by Django 3.2.4 on 2021-06-24 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0008_auto_20210624_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformmodel',
            name='concern',
            field=models.CharField(choices=[('Bantay Serbisyo', 'Bantay Serbisyo'), ('Inquiry', 'Inquiry')], default='N/A', max_length=255),
            preserve_default=False,
        ),
    ]