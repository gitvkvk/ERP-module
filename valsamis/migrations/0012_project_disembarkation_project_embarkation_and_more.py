# Generated by Django 4.0.4 on 2023-08-01 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('valsamis', '0011_customer_pobox_customer_address1_customer_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='disembarkation',
            field=models.TextField(blank=True, help_text='disembarkation port', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='embarkation',
            field=models.TextField(blank=True, help_text='embarkation port', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='project_end_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='project',
            name='project_start_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]