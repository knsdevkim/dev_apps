# Generated by Django 3.1.1 on 2021-02-11 03:54

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210203_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingMemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_no', models.CharField(blank=True, default=core.models.initializeControlNumberTrainingMemo, error_messages={'unique': 'Traning memo control no. is already exists!'}, max_length=250, null=True, unique=True)),
                ('date', models.CharField(blank=True, max_length=150, null=True)),
                ('dear', models.CharField(blank=True, max_length=250, null=True)),
                ('to1', models.CharField(blank=True, max_length=250, null=True)),
                ('to2', models.CharField(blank=True, max_length=250, null=True)),
                ('volume_objective', models.CharField(blank=True, max_length=250, null=True)),
                ('volume_actual', models.CharField(blank=True, max_length=250, null=True)),
                ('volume_percent', models.CharField(blank=True, max_length=250, null=True)),
                ('callproductivity_objective', models.CharField(blank=True, max_length=250, null=True)),
                ('callproductivity_actual', models.CharField(blank=True, max_length=250, null=True)),
                ('callproductivity_percent', models.CharField(blank=True, max_length=250, null=True)),
                ('distribution_objective', models.CharField(blank=True, max_length=250, null=True)),
                ('distribution_actual', models.CharField(blank=True, max_length=250, null=True)),
                ('distribution_percent', models.CharField(blank=True, max_length=250, null=True)),
                ('range_objective', models.CharField(blank=True, max_length=250, null=True)),
                ('range_actual', models.CharField(blank=True, max_length=250, null=True)),
                ('range_percent', models.CharField(blank=True, max_length=250, null=True)),
                ('merchandising_objective', models.CharField(blank=True, max_length=250, null=True)),
                ('merchandising_actual', models.CharField(blank=True, max_length=250, null=True)),
                ('merchandising_percent', models.CharField(blank=True, max_length=250, null=True)),
                ('cycle_objective', models.CharField(blank=True, max_length=250, null=True)),
                ('cycle_actual', models.CharField(blank=True, max_length=250, null=True)),
                ('cycle_percent', models.CharField(blank=True, max_length=250, null=True)),
                ('strength', models.CharField(blank=True, max_length=250, null=True)),
                ('oppurtunities', models.CharField(blank=True, max_length=250, null=True)),
                ('insights', models.CharField(blank=True, max_length=250, null=True)),
                ('actionplan', models.CharField(blank=True, max_length=250, null=True)),
                ('nextstep', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'trainingmemos',
            },
        ),
    ]
