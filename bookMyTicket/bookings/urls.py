from django.urls import path
from . import views
# from . import views

urlpatterns = [
    # Admin Routes
    path('theater_admin/home', views.Admin_Home),
    path('theater_admin/add/city', views.Admin_Add_City),
    path('theater_admin/add/movie', views.Admin_Add_Movie),
    path('theater_admin/add/theater', views.Admin_Add_Theater),
    path('theater_admin/add/show_with_seats', views.Admin_Add_Show_With_Seats),

    # Customer Routes
    path('', views.Cust_Home_Book_Now),
    path('customer/select/city', views.Cust_Select_City),
    path('customer/select/movie', views.Cust_Select_Movie),
    path('customer/select/theater', views.Cust_Select_Theater),
    path('customer/select/show_with_seat', views.Cust_Select_Show_With_Seat),
    path('customer/booking/payment', views.Cust_Booking_Payment),

]
