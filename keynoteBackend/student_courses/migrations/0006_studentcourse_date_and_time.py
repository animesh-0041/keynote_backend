# Generated by Django 4.1.10 on 2023-09-05 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_courses', '0005_remove_studentcourse_date_and_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourse',
            name='date_and_time',
            field=models.DateTimeField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
    ]
