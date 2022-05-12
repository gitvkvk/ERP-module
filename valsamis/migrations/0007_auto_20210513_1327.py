# Generated by Django 3.2.2 on 2021-05-13 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valsamis', '0006_auto_20210513_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='companyname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customername',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='projectname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ship',
            old_name='shipname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subproject',
            old_name='subprojectname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='suppliername',
            new_name='name',
        ),
    ]