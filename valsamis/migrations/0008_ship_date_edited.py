# Generated by Django 4.0.4 on 2023-08-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valsamis', '0007_generalitem_category_generalitem_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='date_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]