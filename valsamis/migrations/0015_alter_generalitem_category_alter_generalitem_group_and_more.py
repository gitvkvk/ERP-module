# Generated by Django 4.0.4 on 2023-08-15 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valsamis', '0014_company_location_info_alter_company_contact_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalitem',
            name='category',
            field=models.CharField(default='testing', max_length=200),
        ),
        migrations.AlterField(
            model_name='generalitem',
            name='group',
            field=models.CharField(default='testing', max_length=200),
        ),
        migrations.AlterField(
            model_name='generalitem',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='generalitem',
            name='subgroup',
            field=models.CharField(default='testing', max_length=200),
        ),
    ]
