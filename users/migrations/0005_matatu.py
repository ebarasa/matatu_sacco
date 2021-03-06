# Generated by Django 2.1.7 on 2019-03-21 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_owner_date_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matatu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reg_number', models.IntegerField()),
                ('reg_year', models.DateTimeField()),
                ('make_and_mode', models.CharField(max_length=100)),
                ('seats', models.IntegerField(choices=[('14', '14'), ('33', '33'), ('60', '60')])),
                ('route', models.CharField(choices=[('eldoret', 'Eldoret'), ('karatina', 'Karatina'), ('nairobi', 'Nairobi'), ('nanyuki', 'Nanyuki'), ('nakuru', 'Nakuru'), ('nyeri', 'Nyeri'), ('thika', 'Thika')], max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='matatu_pics')),
                ('date_added', models.DateTimeField(null=True)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Owner')),
            ],
        ),
    ]
