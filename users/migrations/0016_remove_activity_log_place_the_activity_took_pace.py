# Generated by Django 2.1.7 on 2019-03-22 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_matatu_number_of_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity_log',
            name='Place_the_Activity_took_pace',
        ),
    ]
