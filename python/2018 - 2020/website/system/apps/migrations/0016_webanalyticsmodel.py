# Generated by Django 3.2.4 on 2021-07-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0015_webcontentmodel_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebAnalyticsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.CharField(max_length=300)),
                ('date_visited', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'tbl_web_analytics',
            },
        ),
    ]