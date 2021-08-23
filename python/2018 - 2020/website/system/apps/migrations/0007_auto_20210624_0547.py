# Generated by Django 3.2.4 on 2021-06-24 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_applicationformmodel_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformmodel',
            name='filename',
            field=models.FileField(default='N/A', upload_to='resume/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationformmodel',
            name='type',
            field=models.CharField(choices=[('contact_us', 'CONTACT US'), ('apply_now', 'APPLY NOW')], max_length=20),
        ),
    ]