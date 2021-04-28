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
from django.contrib.auth.models import Group
from .decorators import *

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
        try:
            user = User.objects.get(email=username)
            # user = User.objects.get(username=username)
        except:
            user = None
            
        if user and (check_password(password, user.password) and user.is_active):
            login(request, user)
            return redirect('home')

    return render(request, 'bookings/common/Login.html', context={})


def RegisterPage(request):
    if(request.user.is_authenticated):
        return redirect('home')

    form = CreateUserForm()

    if(request.method == 'POST'):

        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                name=user.username,
                email=user.email
            )

            messages.success(
                request, 'Successfully created account for ' + username)
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


@login_required(login_url='login')
@admin_only
def Admin_Home(request):
    return render(request, 'bookings/webpages/Admin/Admin_Home.html')


@login_required(login_url='login')
@admin_only
def Admin_List_City(request):
    cities = City.objects.all()
    return render(request, 'bookings/webpages/Admin/Admin_List_City.html', {'cities': cities})


@login_required(login_url='login')
@admin_only
def Admin_List_Movie(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/webpages/Admin/Admin_List_Movie.html', {'movies': movies})


@login_required(login_url='login')
@admin_only
def Admin_List_Theater(request):
    theaters = Theater.objects.all()
    return render(request, 'bookings/webpages/Admin/Admin_List_Theater.html', {'theaters': theaters})


@login_required(login_url='login')
@admin_only
def Admin_List_Shows(request, theater_id):

    shows_in_given_theater = Shows.objects.filter(theater=theater_id)
    theater = Theater.objects.get(id=theater_id)
    context = {
        'shows': shows_in_given_theater,
        'count': shows_in_given_theater.count(),
        'theater': theater
    }

    return render(request, 'bookings/webpages/Admin/Admin_List_Shows.html', context)


@login_required(login_url='login')
@admin_only
def Admin_List_Seats(request, show_id):
    seats_in_given_show = Seats.objects.filter(shows=show_id)
    show = Shows.objects.get(id=show_id)

    seat_vals = {
        'seats': seats_in_given_show,
        'seat_count': seats_in_given_show.count(),
        'show': show,
    }
    return render(request, 'bookings/webpages/Admin/Admin_List_Seats.html', {'seat_vals': seat_vals})


@login_required(login_url='login')
@admin_only
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

        # server-side validatation whether seat is booked or not
        if (seat_rec.booking_status != 'BOOKED'):

            # Update Seat's status as Booked, so that seat would show color of Red/Booked for other customers.
            user_id_fk = request.user.id
            customer = Customer.objects.get(user_id=user_id_fk)

            seat_rec.booking_status = 'BOOKED'
            seat_rec.booked_by_cust = customer
            seat_rec.save(update_fields=['booking_status','booked_by_cust'])

            movie_price = seat_rec.shows.movie_shown.markup_price
            th_serv_cost = seat_rec.shows.theater.service_charges or 0

            booking_name = customer.name + " Booked " + seat_rec.shows.movie_shown.name

            # Create Boking, with required vals
            new_book_id = Booking.objects.create(
                name=booking_name,
                amount_paid=movie_price + th_serv_cost,
                on_date=datetime.now(),
                by_customer=customer,
                booked_show=seat_rec.shows
            )
            messages.success(request, 'Booking has created successfully  ')
        else: 
            messages.error(request, 'Can\'t create Booking for this Seat.  ')
        return redirect('select_payment', seat_id=str(seat_id))

# Common Views


def About_Us(request):
    return render(request, 'bookings/common/About_Us.html')


def Contact_Us(request):
    return render(request, 'bookings/common/Contact_Us.html')
