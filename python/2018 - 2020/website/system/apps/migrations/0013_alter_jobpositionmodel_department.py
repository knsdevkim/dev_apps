# Generated by Django 3.2.4 on 2021-07-02 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0012_auto_20210629_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpositionmodel',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='apps.departmentmodel'),
        ),
    ]
