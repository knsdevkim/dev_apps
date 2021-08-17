# Generated by Django 3.1.1 on 2020-12-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_users_auth_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='auth_level',
            field=models.SmallIntegerField(choices=[(1, 'SUPERUSER'), (2, 'ADMIN'), (3, 'TABLET USER')], default=2),
        ),
        migrations.AlterField(
            model_name='users',
            name='employee_code',
            field=models.CharField(error_messages={'unique': 'Employee code is already in use.'}, max_length=10, unique=True),
        ),
    ]
