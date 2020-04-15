# Generated by Django 2.2.7 on 2020-04-11 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handover_form', '0007_auto_20200408_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='handover_details',
            name='file',
            field=models.FileField(default='', upload_to='files'),
        ),
        migrations.AlterField(
            model_name='handover_details',
            name='function',
            field=models.CharField(choices=[('RAVPN', 'RAVPN'), ('DNS', 'DNS'), ('Network Devices', 'Network Devices')], default='RAVPN', max_length=20),
        ),
        migrations.AlterField(
            model_name='handover_details',
            name='problem_statement',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
