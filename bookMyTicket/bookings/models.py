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
	seats_count = models.IntegerField(default=0)
	service_charges = models.IntegerField(default=0)	# add up to movie charges in total bill.

	def __str__(self):
		return self.name


class Movie(models.Model):
	name = models.CharField(max_length=24, null=True, default="")
	markup_price = models.IntegerField(default=0)
	duration_in_min = models.CharField(max_length=24, null=True, default="")
	genre = models.CharField(max_length=24, null=True, default="")
	release_date = models.CharField(max_length=24, null=True, default="")
	language_avail = models.CharField(max_length=24, null=True, default="")
	shown_in_theater = models.ManyToManyField(Theater)

	def __str__(self):
		return self.name


# as of now we consider, each theater has single Auditorim/Hall/Screen and multiple shows in one day.

class Shows(models.Model):
	name = models.CharField(max_length=24, null=True)
	theater = models.ForeignKey(Theater, null=True, on_delete= models.SET_NULL)
	movie_shown = models.ForeignKey(Movie, null=True, on_delete= models.SET_NULL)

	def __str__(self):
		return self.name + " Show at " + self.theater.name

	class Meta:
         db_table = 'Shows'
	

class Seats(models.Model):
	BOOKING_STATUS = (
		('BOOKED', 'BOOKED'),
		('AVAILABLE', 'AVAILABLE'), 
		('RESERVED','RESERVED'),
		('NOT_AVAILABLE','NOT_AVAILABLE')
	)

	seat_code = models.CharField(max_length=24, null=True)
	booking_status = models.CharField(max_length=24, null=True, choices=BOOKING_STATUS, default=BOOKING_STATUS[1][0])
	booked_by_cust = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	shows = models.ForeignKey(Shows, null=True, on_delete= models.SET_NULL)
	
	def __str__(self):
		return self.seat_code	

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


 