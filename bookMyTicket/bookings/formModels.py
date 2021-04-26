from django.forms import ModelForm
from .models import *


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