from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .formModels import *

# 1. Model Form Views for City

def Create_City_Form(request):
    form = City_Form()
    if request.method == 'POST':
        form = City_Form(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('/theater_admin/list/city')
    return render(request, 'bookings/ModelForms/Create_City_Form.html', {'form': form})


def Update_City_Form(request, city_id):
    city_rec = City.objects.get(id=city_id)

    form = City_Form(instance=city_rec)
    if request.method == 'POST':
        form = City_Form(request.POST, instance=city_rec)
        if(form.is_valid):
            form.save()
            return redirect('/theater_admin/list/city')
    return render(request, 'bookings/ModelForms/Create_City_Form.html', {'form': form})


def Delete_City_Form(request, city_id):
    city = City.objects.get(id=city_id)

    if request.method == 'POST' and city:
        city.delete()
        return redirect('/theater_admin/list/city')

    return render(request, 'bookings/ModelForms/Delete_City_Form.html', {'city': city})


# 2. Model Form Views for Movie

def Create_Movie_Form(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/ModelForms/Create_Movie_Form.html', {'movies': movies})


def Update_Movie_Form(request, movie_id):
    movie_rec = Movie.objects.get(id=movie_id)

    form = Movie_Form(instance=movie_rec)
    if request.method == 'POST':
        form = Movie_Form(request.POST, instance=movie_rec)
        if(form.is_valid):
            form.save()
            return redirect('/theater_admin/list/movie')
    return render(request, 'bookings/ModelForms/Create_Movie_Form.html', {'form': form})


def Delete_Movie_Form(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    if request.method == 'POST' and movie:
        movie.delete()
        return redirect('/theater_admin/list/movie')

    return render(request, 'bookings/ModelForms/Delete_Movie_Form.html', {'movie': movie})



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
