# Generated by Django 4.0 on 2021-12-23 01:16

from django.db import migrations, models
import file.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=18, verbose_name='Emp_ID')),
                ('owner', models.CharField(max_length=20, verbose_name='Owner')),
                ('department', models.CharField(max_length=25, verbose_name='Department')),
                ('task', models.CharField(max_length=25, verbose_name='task')),
                ('duedate', models.DateField(verbose_name='Due Date (mm/dd/yy)')),
                ('file', models.FileField(null=True, upload_to=file.models.Employee_Task.nameFile, verbose_name='Report')),
                ('description', models.TextField(max_length=100, verbose_name='Description')),
            ],
            options={
                'db_table': 'employee_task',
            },
        ),
    ]
