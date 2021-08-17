# Generated by Django 3.1.1 on 2021-03-02 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210225_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.CharField(error_messages={'unique': 'Discount is already exists!'}, max_length=3, null=True, unique=True, verbose_name='Discount %')),
            ],
            options={
                'db_table': 'discount',
            },
        ),
        migrations.AddField(
            model_name='invoicemodel',
            name='cash_discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='invoicemodel',
            name='discount',
            field=models.CharField(default='N/D', max_length=3),
        ),
        migrations.AddField(
            model_name='invoicemodel',
            name='discount_person',
            field=models.CharField(default='N/D', max_length=20),
        ),
    ]
