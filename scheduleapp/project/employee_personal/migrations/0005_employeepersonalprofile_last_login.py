# Generated by Django 2.0.5 on 2018-05-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_personal', '0004_employeepersonalprofile_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeepersonalprofile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
