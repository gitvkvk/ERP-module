# Generated by Django 3.2.6 on 2022-02-01 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valsamis', '0018_auto_20220121_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='notes',
            field=models.TextField(blank=True, help_text='any notes for PO?', max_length=1000, null=True),
        ),
    ]