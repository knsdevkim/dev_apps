# Generated by Django 3.2.4 on 2021-06-26 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0010_alter_webcontentmodel_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departmentmodel',
            name='media_token',
        ),
        migrations.RemoveField(
            model_name='mediamodel',
            name='media_token_application',
        ),
        migrations.RemoveField(
            model_name='mediamodel',
            name='media_token_department',
        ),
        migrations.AddField(
            model_name='departmentmodel',
            name='icon',
            field=models.ImageField(default='N/A', null=True, upload_to='dept_icons/'),
        ),
        migrations.AlterField(
            model_name='mediamodel',
            name='filename',
            field=models.FileField(upload_to='web/', verbose_name='Upload Media'),
        ),
    ]
