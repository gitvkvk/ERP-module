# Generated by Django 3.2.2 on 2022-01-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valsamis', '0013_auto_20220121_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
