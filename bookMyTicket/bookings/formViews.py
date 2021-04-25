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
    form = Movie_Form()
    if request.method == 'POST':
        form = Movie_Form(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('/theater_admin/list/movie')
    return render(request, 'bookings/ModelForms/Create_Movie_Form.html', {'form': form})


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




# 3. For Theater

def Create_Theater_Form(request):
    form = Theater_Form()
    if request.method == 'POST':
        form = Theater_Form(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('/theater_admin/list/theater')
    return render(request, 'bookings/ModelForms/Create_Theater_Form.html', {'form': form})


def Update_Theater_Form(request, theater_id):
    theater_rec = Theater.objects.get(id=theater_id)

    form = Theater_Form(instance=theater_rec)
    if request.method == 'POST' and theater_rec:
        form = Theater_Form(request.POST, instance=theater_rec)
        if(form.is_valid):
            form.save()
            return redirect('/theater_admin/list/theater')
    return render(request, 'bookings/ModelForms/Create_Theater_Form.html', {'form': form})


def Delete_Theater_Form(request, theater_id):
    theater = Theater.objects.get(id=theater_id)

    if request.method == 'POST' and theater:
        theater.delete()
        return redirect('/theater_admin/list/theater')

    return render(request, 'bookings/ModelForms/Delete_Theater_Form.html', {'theater': theater})



# 4. For Shows

def Create_Shows_Form(request):
    form = Shows_Form()
    if request.method == 'POST':
        form = Shows_Form(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('/theater_admin/list/shows')
    return render(request, 'bookings/ModelForms/Create_Shows_Form.html', {'form': form})


def Update_Shows_Form(request, shows_id):
    shows_rec = Shows.objects.get(id=shows_id)

    form = Shows_Form(instance=shows_rec)
    if request.method == 'POST' and shows_rec:
        form = Shows_Form(request.POST, instance=shows_rec)
        if(form.is_valid):
            form.save()
            return redirect('/theater_admin/list/shows')
    return render(request, 'bookings/ModelForms/Create_Shows_Form.html', {'form': form})


def Delete_Shows_Form(request, shows_id):
    shows = Shows.objects.get(id=shows_id)

    if request.method == 'POST' and shows:
        shows.delete()
        return redirect('/theater_admin/list/shows')

    return render(request, 'bookings/ModelForms/Delete_Shows_Form.html', {'shows': shows})


