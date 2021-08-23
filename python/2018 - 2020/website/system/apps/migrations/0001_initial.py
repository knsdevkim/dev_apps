# Generated by Django 3.2.4 on 2021-06-22 08:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('mobile', models.CharField(blank=True, max_length=13)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('category_contact_us', models.CharField(blank=True, max_length=150)),
                ('category_apply', models.CharField(blank=True, max_length=150)),
                ('message', models.TextField(blank=True)),
                ('media_token', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('Contact Us', 'CONTACT US'), ('Apply Now', 'APPLY NOW')], max_length=20)),
            ],
            options={
                'db_table': 'tbl_application_forms',
            },
        ),
        migrations.CreateModel(
            name='WebContentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_token', models.TextField()),
                ('location', models.TextField(verbose_name='Location')),
                ('title', models.CharField(max_length=155, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('position', models.CharField(choices=[('Warehouse Picker', 'Warehouse Picker'), ('Helper', 'Helper'), ('Company Driver', 'Company Driver'), ('SHE Officer', 'SHE Officer'), ('Salesman', 'Salesman'), ('Warehouse Coordinator', 'Warehouse Coordinator'), ('Operations Manager - Nestle Professional', 'Operations Manager - Nestle Professional'), ('Accounting Assistant - Inventory  ', 'Accounting Assistant - Inventory  '), ('Maggi Dedicated Seller', 'Maggi Dedicated Seller'), ('Encoder', 'Encoder'), ('Company Nurse', 'Company Nurse'), ('Delivery Driver', 'Delivery Driver'), ('Micro D Seller', 'Micro D Seller'), ('Distributor Key Accounts Specialist - SSF', 'Distributor Key Accounts Specialist - SSF'), ('DKAS Hybrid', 'DKAS Hybrid'), ('Activations & Merchandising Manager', 'Activations & Merchandising Manager'), ('Maggi Dedicated Coordinator', 'Maggi Dedicated Coordinator'), ('Senior Extruck Salesman', 'Senior Extruck Salesman'), ('Distributor Customer Service Supervisor', 'Distributor Customer Service Supervisor'), ('Warehouse Picker', 'Warehouse Picker'), ('Distributor Major Customer Specialist', 'Distributor Major Customer Specialist'), ('Ex-truck Driver', 'Ex-truck Driver'), ('Operations Manager', 'Operations Manager'), ('Warehouse Checker', 'Warehouse Checker'), ('Human Resources Specialist - CompBen', 'Human Resources Specialist - CompBen'), ('Forklift Operator', 'Forklift Operator'), ('Transport Coordinator', 'Transport Coordinator'), ('Accounting Assistant - Inventory', 'Accounting Assistant - Inventory'), ('General Trade Manager', 'General Trade Manager'), ('Warehouse Admin', 'Warehouse Admin'), ('NP Distributor Sales Representative', 'NP Distributor Sales Representative'), ('Accounting Assistant - Cashier', 'Accounting Assistant - Cashier'), ('Accounting Assistant - AR 2', 'Accounting Assistant - AR 2'), ('Senior Extruck Salesman; DKAS-Hybrid', 'Senior Extruck Salesman; DKAS-Hybrid'), ('Utility', 'Utility'), ('Human Resources Manager', 'Human Resources Manager'), ('Accounting Assistant - Inventory ', 'Accounting Assistant - Inventory '), ('Accounting Assistant', 'Accounting Assistant'), ('Accounting Asst- Asset Manage', 'Accounting Asst- Asset Manage'), ('Messenger', 'Messenger'), ('Chief Finance Officer', 'Chief Finance Officer'), ('Micro D Seller ', 'Micro D Seller '), ('Management Trainee', 'Management Trainee'), ('Business Development Officer', 'Business Development Officer'), ('Relief Salesman', 'Relief Salesman'), ('Field Checker', 'Field Checker'), ('Internal Auditor', 'Internal Auditor'), ('Bookkeeper', 'Bookkeeper'), ('Barrista', 'Barrista'), ('Accounting & Finance Officer', 'Accounting & Finance Officer'), ('Sales Support Specialist', 'Sales Support Specialist'), ('IT Champ', 'IT Champ'), ('Motorpool Helper', 'Motorpool Helper'), ('Sales Admin Support', 'Sales Admin Support'), ('Senior Relief Salesman', 'Senior Relief Salesman'), ('Accounting Assistant - IDAS', 'Accounting Assistant - IDAS'), ('HR Specialist - Recruitment', 'HR Specialist - Recruitment'), ('NP Dedicated OM', 'NP Dedicated OM'), ('Corporate Management Trainee', 'Corporate Management Trainee'), ('Accounting Assistant - A/P Clerk (Supplier)', 'Accounting Assistant - A/P Clerk (Supplier)'), ('CEO', 'CEO'), ('Accountant', 'Accountant'), ('Delivery Helper', 'Delivery Helper'), ('HR- Training & Development Officer', 'HR- Training & Development Officer'), ('Micro D Coordinator', 'Micro D Coordinator'), ('Logistics Admin', 'Logistics Admin'), ('HR Specialist  ', 'HR Specialist  '), ('Bad Goods Keeper', 'Bad Goods Keeper'), ('Software Support', 'Software Support'), ('NP Business Development Officer', 'NP Business Development Officer'), ('Accounting Assistant - A/R 1', 'Accounting Assistant - A/R 1'), ('Mechanic', 'Mechanic'), ('Delivery Driver ', 'Delivery Driver '), ('IT Specialist', 'IT Specialist'), ('Supply Chain Manager', 'Supply Chain Manager'), ('Employee Relations/Executive Assistant', 'Employee Relations/Executive Assistant'), ('Technical Support', 'Technical Support')], max_length=255, verbose_name='Position')),
                ('date_posted', models.DateField(default=django.utils.timezone.now, verbose_name='Date Posted')),
                ('author', models.CharField(max_length=150, verbose_name='Author')),
                ('site_map', models.URLField(blank=True, max_length=300, verbose_name='Site URL')),
                ('ne_type', models.CharField(choices=[('News', 'News'), ('Events', 'Events')], max_length=150, verbose_name='Content Type')),
                ('type', models.CharField(choices=[('branches', 'BRANCHES'), ('news_and_events', 'NEWS AND EVENTS'), ('job_position', 'JOB POSITION'), ('employee', 'EMPLOYEE')], max_length=150)),
            ],
            options={
                'db_table': 'tbl_web_contents',
            },
        ),
        migrations.CreateModel(
            name='MediaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.FileField(upload_to='dev_storage/', verbose_name='Upload Media')),
                ('date_uploaded', models.DateField(auto_now=True)),
                ('media_token_application', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.applicationformmodel')),
                ('media_token_web_contents', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.webcontentmodel')),
            ],
            options={
                'db_table': 'tbl_media',
            },
        ),
    ]
