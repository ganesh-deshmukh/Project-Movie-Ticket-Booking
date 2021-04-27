from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .formModels import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required


# Authentication routes
def LoginPage(request):
    if(request.user.is_authenticated):
            return redirect('home')
            
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # TODO Debug: why this authenticate doesn't work but other check password works?
        # user = authenticate(request, email=username, password=password)
        # if user:
            # login(request, password)
            # redirect('home')

        user = User.objects.get(email=username)
        if (check_password(password, user.password) and user.is_active):
            login(request, user)
            return redirect('home')
    
    return render(request, 'bookings/common/Login.html', context={})

def RegisterPage(request):
    if(request.user.is_authenticated):
        return redirect('home')
    form = CreateUserForm()

    if(request.method == 'POST'):
            

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request, 'Successfully created account for ' + user)
            return redirect('/login')
        else:
            messages.success(request, 'Can\'t create account for User.  ')

    context = {'form': form}

    return render(request, 'bookings/common/Register.html', context)

@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('/login')

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
@login_required(login_url='login')
def Cust_Home_Book_Now(request):
    return render(request, 'bookings/webpages/Customer/Cust_Home_Book_Now.html')

 # for filtering

@login_required(login_url='login')
def Cust_Select_City(request):
    city_name = request.GET.get('city_name')
    if city_name:
        cities = City.objects.filter(name__icontains=city_name)

    else:
        cities = City.objects.all()

    return render(request, 'bookings/webpages/Customer/Cust_Select_City.html', {'cities': cities})


@login_required(login_url='login')
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


@login_required(login_url='login')
def Cust_Select_Theater(request, city_id, movie_id):

    theaters = []
    # theaters_in_city = Theater.objects.filter(located_city=city_id)

    for show in Shows.objects.all():
        if(str(show.theater.located_city.id) == city_id
           and (str(show.movie_shown.id) == movie_id)
           and show.theater not in theaters):

            theaters.append(show.theater)

    context = {
        'theaters': theaters,
        'movie_id': movie_id,
    }
    return render(request, 'bookings/webpages/Customer/Cust_Select_Theater.html', context)


@login_required(login_url='login')
def Cust_Select_Show(request, theater_id, movie_id):
    shows = []
    for show in Shows.objects.all():
        if(str(show.theater.id) == theater_id and str(show.movie_shown.id) == movie_id):
            shows.append(show)
    return render(request, 'bookings/webpages/Customer/Cust_Select_Show.html', {'shows': shows})


@login_required(login_url='login')
def Cust_Select_Seat(request, show_id):
    seats = Seats.objects.filter(shows=show_id)
    show = Shows.objects.get(id=show_id)
    avail_seats = 0

    for seat in seats:
        if(seat.booking_status == 'AVAILABLE'):
            avail_seats += 1

    context = {
        'seats': seats,
        'avail_seats': avail_seats,
        'show': show,
    }

    return render(request, 'bookings/webpages/Customer/Cust_Select_Seat.html', context)


@login_required(login_url='login')
def Cust_Booking_Payment(request, seat_id):
    seat_rec = Seats.objects.get(id=seat_id)

    if(request.method == 'GET'):
        return render(request, 'bookings/webpages/Customer/Cust_Booking_Payment.html', {'seat': seat_rec})
    elif request.user.is_authenticated:
        print("authenticated")
        seat_vals = {
            'booking_status': 'BOOKED',
            'booked_by_cust': request.user.id or ''
        }
        seat_rec.booking_status = 'BOOKED'
        seat_rec.booked_by_cust = request.user.id
        seat_rec.save()

        movie_price = seat_rec.shows.movie_shown.markup_price
        th_serv_cost = seat_rec.shows.theater.service_charges or 0

        print("****************** request.user.customer.id = ", request.user.customer.id)
        booking_vals = {
            'id': None,
            'name': 'Booking via Website',
            'amount_paid': movie_price + th_serv_cost,
            'on_date': datetime.now(),
            'by_customer': request.user.id,
            'booked_show': seat_rec.shows.id
        }

        # booking_rec = Booking.objects.filter().last()
        # booking_rec.id.update(booking_vals)
        # booking_rec.save()

    return redirect('/')

# Common Views


def About_Us(request):
    return render(request, 'bookings/common/About_Us.html')


def Contact_Us(request):
    return render(request, 'bookings/common/Contact_Us.html')

