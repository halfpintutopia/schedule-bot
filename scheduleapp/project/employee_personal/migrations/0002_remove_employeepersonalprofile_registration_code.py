# Generated by Django 2.0.5 on 2018-05-15 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_personal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeepersonalprofile',
            name='registration_code',
        ),
    ]
