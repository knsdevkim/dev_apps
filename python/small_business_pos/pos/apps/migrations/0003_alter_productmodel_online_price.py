# Generated by Django 3.2.5 on 2021-08-02 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20210802_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='online_price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='if applicable', max_digits=15, verbose_name='Online Price'),
        ),
    ]
