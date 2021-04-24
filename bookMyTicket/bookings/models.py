from django.db import models
from django.contrib.auth.models import User

# there might be two cities with same names, so we will assign each city a unique PIN-Code later.


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=24, null=True)
	phone = models.CharField(max_length=10, null=True)
	email = models.CharField(max_length=50, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class City(models.Model):
	name = models.CharField(max_length=20, null=True)
	pincode = models.CharField(max_length=10, null=True)

	def __str__(self):
		return self.name

	class Meta:
    	 db_table = 'Cities'


class Theater(models.Model):
	name = models.CharField(max_length=24, null=True)
	description = models.CharField(max_length=100, null=True)
	located_city = models.ForeignKey(City, null=True,on_delete=models.CASCADE)
    # seatsCount = models.IntegerField(default=0)

	def __str__(self):
		return self.name


class Movie(models.Model):
	name = models.CharField(max_length=24, null=True)
	shown_in_theater = models.ManyToManyField(Theater)
	markup_price = models.IntegerField(default=0)
	duration_in_min = models.CharField(max_length=24, null=True)
	genre = models.CharField(max_length=24, null=True)
	release_date = models.CharField(max_length=24, null=True)
	language_avail = models.CharField(max_length=24, null=True)

	def __str__(self):
		return self.name


class Shows(models.Model):
	name = models.CharField(max_length=24, null=True)
	theater = models.ForeignKey(Theater, null=True, on_delete= models.SET_NULL)
	movie_shown = models.ForeignKey(Movie, null=True, on_delete= models.SET_NULL)

	def __str__(self):
		return self.name

	class Meta:
         db_table = 'Shows'
	

class Seats(models.Model):
	BOOKING_STATUS = (
		('BOOKED', 'BOOKED'),
		('AVAILABLE', 'AVAILABLE'), 
		('RESERVED','RESERVED'),
		('NOT_AVAILABLE','NOT_AVAILABLE')
	)

	seq_code = models.CharField(max_length=24, null=True)
	booking_status = models.CharField(max_length=24, null=True, choices=BOOKING_STATUS, default=BOOKING_STATUS[1][0])
	booked_by_cust = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	avail_in_shows = models.ManyToManyField(Shows)

	def __str__(self):
		return self.name	

	class Meta:
		db_table = 'Seats'


class Booking(models.Model):
    name = models.CharField(max_length=24, null=True)
    amount_paid = models.IntegerField(null=True)
    on_date = models.CharField(max_length=24, null=True)
    by_customer = models.OneToOneField(Customer, null=True, on_delete=models.SET_NULL)
    booked_show = models.OneToOneField(Shows, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


 