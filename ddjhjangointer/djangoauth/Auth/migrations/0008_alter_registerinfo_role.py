# Generated by Django 5.0.2 on 2024-08-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0007_registerinfo_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerinfo',
            name='role',
            field=models.CharField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor')], default='', max_length=10),
        ),
    ]
