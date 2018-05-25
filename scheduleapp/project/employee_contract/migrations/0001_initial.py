# Generated by Django 2.0.5 on 2018-05-15 21:10

from django.db import migrations, models
import django.db.models.deletion
import project.api.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeContractProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('contract_started', models.DateTimeField(auto_now_add=True, null=True, verbose_name='joined_date')),
                ('contract_number', models.CharField(default=project.api.helpers.code_generator, max_length=15, unique=True, verbose_name='contract number')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_personal.EmployeePersonalProfile', verbose_name='employee')),
            ],
        ),
    ]