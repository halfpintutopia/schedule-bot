# Generated by Django 2.0.5 on 2018-05-24 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_personal', '0006_auto_20180521_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeepersonalprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employeepersonalprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employeepersonalprofile',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='employeepersonalprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='employeepersonalprofile',
            name='password',
        ),
        migrations.AlterField(
            model_name='employeepersonalprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_profile', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
