# Generated by Django 5.0.2 on 2024-08-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0010_alter_registerinfo_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerinfo',
            name='role',
            field=models.CharField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor')], default='patient', max_length=20),
        ),
    ]
