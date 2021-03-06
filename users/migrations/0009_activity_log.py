# Generated by Django 2.1.7 on 2019-03-21 14:11

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_finance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Time_of_record', models.DateTimeField()),
                ('Activity_log_type', models.CharField(choices=[('trips', 'Trips'), ('traffic_offence', 'Traffic_offence'), ('breakdown', 'Breakdown'), ('repair', 'Repair'), ('fuel', 'Fuel'), ('milage', 'Milage'), ('others', 'Others')], max_length=100)),
                ('Activity_log_details', models.CharField(max_length=500)),
                ('number_of_trips_made_until_now', models.IntegerField()),
                ('Place_the_Activity_took_pace', models.CharField(max_length=100)),
                ('Date_and_Time_the_Activity_took_place', models.DateTimeField()),
                ('Where_maintanance_happened', models.CharField(max_length=100)),
                ('Date_Time_maintanance_happened', models.DateTimeField()),
                ('Who_did_Maintanance', models.CharField(max_length=100)),
                ('contacts_of_who_did_the_repair', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('image_before_maintanance', models.ImageField(default='default.jpg', upload_to='maintanance_pics')),
                ('image_after_maintanance', models.ImageField(default='default.jpg', upload_to='maintanance_pics')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('reciept', models.ImageField(default='default.jpg', upload_to='reciept_pics')),
                ('matatu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Matatu')),
            ],
        ),
    ]
