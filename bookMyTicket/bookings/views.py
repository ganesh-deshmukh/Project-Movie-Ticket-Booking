from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Admin Views

def Admin_Home(request):
    return render(request, 'bookings/Admin_Home.html')


def Admin_Add_City(request):
    cities = City.objects.all()
    return render(request, 'bookings/Admin_Add_City.html', {'cities': cities})


def Admin_Add_Movie(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/Admin_Add_Movie.html', {'movies': movies})


def Admin_Add_Theater(request):
    theaters = Theater.objects.all()
    return render(request, 'bookings/Admin_Add_Theater.html', {'theaters': theaters})


def Admin_Add_Shows(request, theater_id):
    shows_in_given_theater = Shows.objects.filter(theater=theater_id)
    theater_rec = Theater.objects.get(id=theater_id)
    return render(request, 'bookings/Admin_Add_Shows.html', {'shows': shows_in_given_theater, 'theater_name': theater_rec.name})


def Admin_Add_Seats(request, show_id):
    seats_in_given_show = Seats.objects.filter(shows=show_id)
    show_rec = Shows.objects.get(id=show_id)
    
    seat_vals = {
        'seats': seats_in_given_show, 
        'show_name': show_rec.name,
        'theater_name': show_rec.theater.name,
    }
    return render(request, 'bookings/Admin_Add_Seats.html', {'seat_vals': seat_vals})


# Customer Views

def Cust_Home_Book_Now(request):
    return render(request, 'bookings/Cust_Home_Book_Now.html')


def Cust_Select_City(request):
    return render(request, 'bookings/Cust_Select_City.html')


def Cust_Select_Movie(request):
    return render(request, 'bookings/Cust_Select_Movie.html')


def Cust_Select_Theater(request):
    return render(request, 'bookings/Cust_Select_Theater.html')


def Cust_Select_Show(request):
    return render(request, 'bookings/Cust_Select_Show.html')


def Cust_Select_Seat(request):
    return render(request, 'bookings/Cust_Select_Seat.html')


def Cust_Booking_Payment(request):
    return render(request, 'bookings/Cust_Booking_Payment.html')



# Common Views

def About_Us(request):
    return render(request, 'bookings/common/About_Us.html')


def Contact_Us(request):
    return render(request, 'bookings/common/Contact_Us.html')