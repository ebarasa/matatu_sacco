# Generated by Django 2.1.7 on 2019-03-21 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190321_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('finance_type', models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=100)),
                ('details', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('reciept', models.ImageField(default='default.jpg', upload_to='reciept_pics')),
                ('matatu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Matatu')),
            ],
        ),
    ]
