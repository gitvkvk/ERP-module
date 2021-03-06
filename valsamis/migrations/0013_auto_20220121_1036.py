# Generated by Django 3.2.2 on 2022-01-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valsamis', '0012_auto_20220121_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='typeship',
            field=models.CharField(blank=True, choices=[('c', 'Cruise ship'), ('t', 'Tanker'), ('o', 'Other')], default='c', help_text='What type of ship is it', max_length=1),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(help_text='Enter the supplier name', max_length=200),
        ),
    ]
