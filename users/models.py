from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			image.thumbnail(output_size)
			img.save(self.image.path)


class Owner(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=100)
	id_number = models.IntegerField()
	phone_number = PhoneNumberField()
	date_joined = models.DateTimeField(null=True)

	def __str__(self):
		return self.full_name




class Matatu(models.Model):
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	reg_number = models.IntegerField()
	reg_year = models.DateTimeField()
	make_and_mode =models.CharField(max_length=100)
	number_of_seats = models.IntegerField(null=True)
	route = models.CharField(max_length=100, choices=(
		('eldoret', 'Eldoret'),
		('karatina', 'Karatina'),
		('nairobi', 'Nairobi'),
		('nanyuki', 'Nanyuki'),
		('nakuru', 'Nakuru'),
		('nyeri', 'Nyeri'),
		('thika', 'Thika')
	))
	image = models.ImageField(default='default.jpg', upload_to='matatu_pics')
	date_added = models.DateTimeField(null=True)

	def __str__(self):
		return self.name


class Crew(models.Model):
	matatu = models.ForeignKey(Matatu, on_delete=models.CASCADE)
	crew_type = models.CharField(max_length=100, choices = (
		('driver', 'Driver'),
		('tout', 'Tout')
	)) 
	full_name = models.CharField(max_length=100)
	id_number = models.IntegerField()
	phone_number = PhoneNumberField()
	age = models.IntegerField()
	driver_license_type = models.CharField(max_length=100, choices = (
		('category_a', 'Category A'),
		('category_b', 'Category B'),
		('category_c', 'Category C')
	))  
	driver_license_number = models.CharField(max_length=100)
	image = models.ImageField(default='default.jpg', upload_to='crew_pics')
	date_added = models.DateTimeField(null=True)


	def __str__(self):
		return self.full_name


class Finance(models.Model):
	matatu = models.ForeignKey(Matatu, on_delete=models.CASCADE)
	date_time = models.DateTimeField()
	finance_type = models.CharField(max_length=100, choices = (
		('income', 'Income'),
		('expense', 'Expense')
	))
	details = models.CharField(max_length=200)
	amount = models.DecimalField(decimal_places=2, max_digits=100)
	reciept = models.ImageField(default='default.jpg', upload_to='reciept_pics')

	def __str__(self):
		return self.details

class Activity_log(models.Model):
	matatu = models.ForeignKey(Matatu, on_delete=models.CASCADE)
	Date_Time_of_record = models.DateTimeField() 
	Activity_log_type = models.CharField(max_length=100, choices = (
		('trips', 'Trips'),
		('traffic_offence', 'Traffic_offence'),
		('breakdown', 'Breakdown'),
		('repair', 'Repair'),
		('fuel', 'Fuel'),
		('milage', 'Milage'),
		('others', 'Others')
	))
	Activity_log_details = models.CharField(max_length=500)
	number_of_trips_made_until_now = models.IntegerField(null=True) 
	Place_the_Activity_happened = models.CharField(max_length=100, null=True)
	Date_and_Time_the_Activity_took_place = models.DateTimeField(null=True)
	Where_maintanance_happened =  models.CharField(max_length=100)
	Date_Time_maintanance_happened = models.DateTimeField()
	Who_did_Maintanance = models.CharField(max_length=100)
	contacts_of_who_did_the_repair =  PhoneNumberField()
	image_before_maintanance = models.ImageField(default='default.jpg', upload_to='maintanance_pics')
	image_after_maintanance = models.ImageField(default='default.jpg', upload_to='maintanance_pics')
	amount = models.DecimalField(decimal_places=2, max_digits=100)
	reciept = models.ImageField(default='default.jpg', upload_to='reciept_pics')

	def __str__(self):
		return self. Activity_log_type

