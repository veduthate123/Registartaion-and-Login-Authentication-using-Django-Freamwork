# Generated by Django 5.0.2 on 2024-08-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Profile_Picture', models.CharField(max_length=50)),
                ('Username', models.CharField(max_length=50)),
                ('Email_Id', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Confirm_Password', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('Line1', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Pincode', models.CharField(max_length=50)),
            ],
        ),
    ]