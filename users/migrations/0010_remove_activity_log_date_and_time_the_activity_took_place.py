# Generated by Django 2.1.7 on 2019-03-22 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_activity_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity_log',
            name='Date_and_Time_the_Activity_took_place',
        ),
    ]
