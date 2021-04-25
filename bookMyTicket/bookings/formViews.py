from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Model Form Views for Updation

def Create_City_Form(request):
    return render(request, 'bookings/ModelForms/Create_City_Form.html')


def Create_Movie_Form(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/ModelForms/Create_Movie_Form.html', {'movies': movies})


def Create_Theater_Form(request):
    theaters = Theater.objects.all()
    return render(request, 'bookings/ModelForms/Create_Theater_Form.html', {'theaters': theaters})


def Create_Shows_Form(request, theater_id):
    shows_in_given_theater = Shows.objects.filter(theater=theater_id)
    theater_rec = Theater.objects.get(id=theater_id)
    return render(request, 'bookings/ModelForms/Create_Shows_Form.html', {'shows': shows_in_given_theater, 'theater_name': theater_rec.name})


def Create_Seats_Form(request, show_id):
    seats_in_given_show = Seats.objects.filter(shows=show_id)
    show_rec = Shows.objects.get(id=show_id)
    
    seat_vals = {
        'seats': seats_in_given_show, 
        'seat_count': seats_in_given_show.count(), 
        'show_name': show_rec.name,
        'theater_name': show_rec.theater.name,
    }
    return render(request, 'bookings/ModelForms/Create_Seats_Form.html', {'seat_vals': seat_vals})
