# Generated by Django 3.2.2 on 2021-05-10 21:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('valsamis', '0002_rename_companyname_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='branches',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='valsamis.branches'),
        ),
        migrations.CreateModel(
            name='CompanyInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('branches', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='valsamis.branches')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='valsamis.company')),
            ],
        ),
    ]
