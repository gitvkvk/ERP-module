# Generated by Django 3.2.6 on 2022-01-22 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valsamis', '0016_itemregister_purchaseorder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemRegister',
            new_name='MaterialItemRegister',
        ),
        migrations.AlterField(
            model_name='ship',
            name='typeship',
            field=models.CharField(blank=True, choices=[('c', 'Cruise ship'), ('t', 'Tanker'), ('p', 'Passenger Ship'), ('o', 'Other')], default='c', help_text='What type of ship is it', max_length=1),
        ),
    ]
