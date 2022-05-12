# Generated by Django 3.2.2 on 2021-05-13 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('valsamis', '0005_auto_20210513_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(help_text='Enter the customer name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppliername', models.CharField(help_text='Enter the customer name', max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='companyname',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='projectname',
        ),
        migrations.RenameField(
            model_name='ship',
            old_name='name',
            new_name='shipname',
        ),
        migrations.RemoveField(
            model_name='ship',
            name='shiptype',
        ),
        migrations.RemoveField(
            model_name='ship',
            name='status',
        ),
        migrations.AddField(
            model_name='ship',
            name='typeship',
            field=models.CharField(blank=True, choices=[('c', 'Cruise ship'), ('t', 'Tanker')], default='c', help_text='What type of ship is it', max_length=1),
        ),
        migrations.CreateModel(
            name='subproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subprojectname', models.CharField(help_text='Enter the project name', max_length=200)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='valsamis.company')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='valsamis.project')),
                ('ship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='valsamis.ship')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='valsamis.customer'),
        ),
    ]
