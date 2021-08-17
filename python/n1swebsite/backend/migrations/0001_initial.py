# Generated by Django 3.1.1 on 2020-10-17 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('mission', models.TextField()),
                ('vision', models.TextField()),
            ],
            options={
                'db_table': 'about',
            },
        ),
        migrations.CreateModel(
            name='BranchModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='no-image.png', upload_to='branch/')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('phonenumber', models.CharField(default='N/A', max_length=20)),
                ('email', models.EmailField(default='N/A', max_length=254)),
                ('address', models.TextField(default='N/A')),
            ],
            options={
                'db_table': 'branch',
            },
        ),
        migrations.CreateModel(
            name='CareersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('vacants', models.IntegerField()),
            ],
            options={
                'db_table': 'careers',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='ContactusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('category', models.CharField(choices=[('Inquiry', 'Inquiry'), ('Feedback', 'Feedback'), ('Review', 'Review')], max_length=20)),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'contactus',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='MilestoneModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(default='no-image.png', upload_to='milestone')),
                ('date', models.DateField()),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'milestone',
            },
        ),
        migrations.CreateModel(
            name='NewsEventModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='no-image.png', upload_to='newsevent/')),
                ('title', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('News', 'News'), ('Event', 'Event')], max_length=20)),
            ],
            options={
                'db_table': 'newsevent',
            },
        ),
        migrations.CreateModel(
            name='SiteSettingsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=150)),
                ('is_display', models.BooleanField()),
            ],
            options={
                'db_table': 'sitesettings',
            },
        ),
        migrations.CreateModel(
            name='SlideshowModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='no-image.png', upload_to='slideshow/')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('status', models.CharField(blank=True, choices=[('In Use', 'In Use'), ('Not Use', 'Not Use')], default='In Use', max_length=20)),
            ],
            options={
                'db_table': 'slideshow',
            },
        ),
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'videos',
            },
        ),
    ]