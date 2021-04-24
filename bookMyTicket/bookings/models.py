from django.db import models

# there might be two cities with same names, so we will assign each city a unique PIN-Code later.


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=24, null=True)
	phone = models.CharField(max_length=24, null=True)
	email = models.CharField(max_length=24, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class City(models.Model):
	name = models.CharField(max_length=24, null=True)
    movie = models.ManyToManyField(Movie)
    theater = models.ManyToManyField(Theater)

    def __str__(self):
        return self.name


class Movie(models.Model):
	name = models.CharField(max_length=24, null=True)

	def __str__(self):
		return self.name



class Theater(models.Model):
	name = models.CharField(max_length=24, null=True)

	def __str__(self):
		return self.name



class Booking(models.Model):
    name = models.CharField(max_length=24, null=True)
    
    def __str__(self):
        return self.name


 