# Generated by Django 4.1.3 on 2022-12-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('fee', models.IntegerField()),
                ('duration', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(max_length=100)),
                ('trainer_name', models.CharField(max_length=100)),
                ('trainer_exp', models.CharField(max_length=100)),
                ('training_mode', models.CharField(max_length=100)),
            ],
        ),
    ]
