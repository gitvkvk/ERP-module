# Generated by Django 4.0.4 on 2023-01-13 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the company name', max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the customer name', max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='generalitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the general item name', max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Enter the project name', max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, help_text='any notes for the project', max_length=1000, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='valsamis.company')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='valsamis.customer')),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the supplier name', max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the ship name', max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(default=0)),
                ('reviewed', models.BooleanField(default=0)),
                ('typeship', models.CharField(blank=True, choices=[('c', 'Cruise ship'), ('t', 'Tanker'), ('p', 'Passenger Ship'), ('o', 'Other')], default='c', help_text='What type of ship is it', max_length=1)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='valsamis.company')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pochoices', models.CharField(blank=True, choices=[('M', 'Material'), ('L', 'Logistics'), ('T', 'Travel'), ('O', 'Other')], default='M', help_text='Type of PO', max_length=1)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, help_text='any notes for PO?', max_length=1000, null=True)),
                ('customer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='valsamis.customer')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valsamis.project')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valsamis.supplier')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='ship',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='valsamis.ship'),
        ),
        migrations.CreateModel(
            name='MaterialItemRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('item_description', models.TextField(help_text='Enter the description of the item', max_length=1000, null=True)),
                ('unit', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=10, max_digits=19)),
                ('currency', models.CharField(choices=[('U', 'US Dollars'), ('E', 'Euros'), ('P', 'Pesos')], default='U', max_length=1)),
                ('supplier_code', models.CharField(blank=True, help_text='Enter Supplier Code if you can', max_length=40)),
                ('notes', models.TextField(help_text='Enter any notes for this item', max_length=1000)),
                ('PurchaseOrder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='valsamis.purchaseorder')),
                ('generalitem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='valsamis.generalitem')),
            ],
        ),
    ]
