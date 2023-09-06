# Generated by Django 4.1.10 on 2023-09-01 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('credits', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('course_code', models.CharField(max_length=10, unique=True)),
                ('instructor_name', models.CharField(max_length=255)),
                ('instructor_id', models.PositiveIntegerField()),
            ],
        ),
    ]
