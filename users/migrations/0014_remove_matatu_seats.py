# Generated by Django 2.1.7 on 2019-03-22 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_activity_log_number_of_trips_made_until_now'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matatu',
            name='seats',
        ),
    ]