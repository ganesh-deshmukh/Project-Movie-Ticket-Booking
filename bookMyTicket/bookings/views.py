from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Admin Views

def Admin_Home(request):
    return render(request, 'bookings/webpages/Admin/Admin_Home.html')


def Admin_List_City(request):
    cities = City.objects.all()
    return render(request, 'bookings/webpages/Admin/Admin_List_City.html', {'cities': cities})


def Admin_List_Movie(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/webpages/Admin/Admin_List_Movie.html', {'movies': movies})


def Admin_List_Theater(request):
    theaters = Theater.objects.all()
    return render(request, 'bookings/webpages/Admin/Admin_List_Theater.html', {'theaters': theaters})


def Admin_List_Shows(request, theater_id):

    shows_in_given_theater = Shows.objects.filter(theater=theater_id)
    theater = Theater.objects.get(id=theater_id)
    context = {
        'shows': shows_in_given_theater,
        'count': shows_in_given_theater.count(),
        'theater': theater
    }

    return render(request, 'bookings/webpages/Admin/Admin_List_Shows.html', context)


def Admin_List_Seats(request, show_id):
    seats_in_given_show = Seats.objects.filter(shows=show_id)
    show = Shows.objects.get(id=show_id)

    seat_vals = {
        'seats': seats_in_given_show,
        'seat_count': seats_in_given_show.count(),
        'show': show,
    }
    return render(request, 'bookings/webpages/Admin/Admin_List_Seats.html', {'seat_vals': seat_vals})


def Admin_Seat_Details(request, seat_id):
    seat = Seats.objects.get(id=seat_id)

    return render(request, 'bookings/webpages/Admin/Admin_Seat_Details.html', {'seat': seat})


# Customer Views

def Cust_Home_Book_Now(request):
    return render(request, 'bookings/webpages/Customer/Cust_Home_Book_Now.html')

 # for filtering

def Cust_Select_City(request):
    city_name = request.GET.get('city_name')
    if city_name:
        cities = City.objects.filter(name__icontains=city_name)

    else:
        cities = City.objects.all()

    return render(request, 'bookings/webpages/Customer/Cust_Select_City.html', {'cities': cities})


def Cust_Select_Movie(request, city_id):
    movies = []
    # theaters = Theater.objects.filter(located_city=city_id)

    shows = Shows.objects.all()

    for show in shows:
        print("city_id = ", city_id)
        print("show.theater.located_city.id = ",
              str(show.theater.located_city.id))
        if(str(show.theater.located_city.id) == str(city_id)):

            if(show.movie_shown not in movies):
                movies.append(show.movie_shown)

    print("movies = ", movies)

    return render(request, 'bookings/webpages/Customer/Cust_Select_Movie.html', {"movies": movies})


def Cust_Select_Theater(request):
    return render(request, 'bookings/webpages/Customer/Cust_Select_Theater.html')


def Cust_Select_Show(request):
    return render(request, 'bookings/webpages/Customer/Cust_Select_Show.html')


def Cust_Select_Seat(request):
    return render(request, 'bookings/webpages/Customer/Cust_Select_Seat.html')


def Cust_Booking_Payment(request):
    return render(request, 'bookings/webpages/Customer/Cust_Booking_Payment.html')


# Common Views

def About_Us(request):
    return render(request, 'bookings/common/About_Us.html')


def Contact_Us(request):
    return render(request, 'bookings/common/Contact_Us.html')
