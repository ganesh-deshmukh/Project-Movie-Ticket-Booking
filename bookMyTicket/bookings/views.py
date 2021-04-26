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
    movie_name = request.GET.get('movie_name') or ''
    movies = []
    shows = Shows.objects.all()

    for show in shows:
        if(str(show.theater.located_city.id) == str(city_id) and (show.movie_shown not in movies)):
            if movie_name:
                if (movie_name.lower() in show.movie_shown.name.lower()):
                    movies.append(show.movie_shown)
            else:
                movies.append(show.movie_shown)

    context = {
        "movies": movies,
        "city_id": city_id,
    }
    return render(request, 'bookings/webpages/Customer/Cust_Select_Movie.html', context)


def Cust_Select_Theater(request, city_id, movie_id):

    theaters = []
    theaters_in_city = Theater.objects.filter(located_city=city_id)

    for show in Shows.objects.all():
        if(str(show.theater.located_city.id) == city_id
           and (str(show.movie_shown.id) == movie_id)
           and show.theater not in theaters):

            theaters.append(show.theater)

    return render(request, 'bookings/webpages/Customer/Cust_Select_Theater.html', {'theaters': theaters})


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
