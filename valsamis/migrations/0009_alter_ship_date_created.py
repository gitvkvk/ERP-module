# Generated by Django 4.0.4 on 2023-08-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valsamis', '0008_ship_date_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
