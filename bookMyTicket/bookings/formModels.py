from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class City_Form(ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class Movie_Form(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class Theater_Form(ModelForm):
    class Meta:
        model = Theater
        fields = '__all__'


class Shows_Form(ModelForm):
    class Meta:
        model = Shows
        fields = '__all__'


class Seats_Form(ModelForm):
    class Meta:
        model = Seats
        fields = ('booking_status', 'shows')


# For Payment with Seat ID.

class PaymentForm(ModelForm):
    class Meta:
        model = Booking
        fields = ()


# Auth Forms

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

