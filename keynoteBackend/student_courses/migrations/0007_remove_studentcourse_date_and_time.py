# Generated by Django 4.1.10 on 2023-09-05 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_courses', '0006_studentcourse_date_and_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentcourse',
            name='date_and_time',
        ),
    ]
