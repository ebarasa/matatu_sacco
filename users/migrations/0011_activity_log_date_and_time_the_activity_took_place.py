# Generated by Django 2.1.7 on 2019-03-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_activity_log_date_and_time_the_activity_took_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity_log',
            name='Date_and_Time_the_Activity_took_place',
            field=models.DateTimeField(null=True),
        ),
    ]
