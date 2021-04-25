from django.shortcuts import render
from django.http import HttpResponse

# Admin Views

def Admin_Home(request):
    return render(request, 'bookings/Admin_Home.html')


def Admin_Add_City(request):
    return render(request, 'bookings/Admin_Add_City.html')


def Admin_Add_Movie(request):
    return render(request, 'bookings/Admin_Add_Movie.html')


def Admin_Add_Theater(request):
    return render(request, 'bookings/Admin_Add_Theater.html')


def Admin_Add_Show_With_Seats(request):
    return render(request, 'bookings/Admin_Add_Show_With_Seats.html')


# Customer Views

def Cust_Home_Book_Now(request):
    return render(request, 'bookings/Cust_Home_Book_Now.html')


def Cust_Select_City(request):
    return render(request, 'bookings/Cust_Select_City.html')


def Cust_Select_Movie(request):
    return render(request, 'bookings/Cust_Select_Movie.html')


def Cust_Select_Theater(request):
    return render(request, 'bookings/Cust_Select_Theater.html')


def Cust_Select_Show_With_Seat(request):
    return render(request, 'bookings/Cust_Select_Show_With_Seat.html')


def Cust_Booking_Payment(request):
    return render(request, 'bookings/Cust_Booking_Payment.html')



# Common Views

def About_Us(request):
    return render(request, 'bookings/common/About_Us.html')


def Contact_Us(request):
    return render(request, 'bookings/common/Contact_Us.html')