# Generated by Django 3.2.2 on 2022-01-21 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valsamis', '0010_auto_20220121_1027'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PO',
            new_name='PurchaseOrder',
        ),
    ]
