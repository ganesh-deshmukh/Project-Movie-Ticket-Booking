from django.urls import path
from . import views
# from . import views

urlpatterns = [
    # Admin Routes
    path('theater_admin/home', views.Admin_Home),
    path('theater_admin/add/city', views.Admin_List_City),
    path('theater_admin/add/movie', views.Admin_List_Movie),
    path('theater_admin/add/theater', views.Admin_List_Theater),
    path('theater_admin/add/shows/<str:theater_id>/', views.Admin_List_Shows),
    path('theater_admin/add/seats/<str:show_id>/', views.Admin_List_Seats),
    path('theater_admin/seats/details/<str:seat_id>/', views.Admin_Seat_Details),


    # Customer Routes
    path('', views.Cust_Home_Book_Now),
    path('customer/select/city', views.Cust_Select_City),
    path('customer/select/movie', views.Cust_Select_Movie),
    path('customer/select/theater', views.Cust_Select_Theater),
    path('customer/select/show', views.Cust_Select_Show),
    path('customer/select/seat', views.Cust_Select_Seat),
    path('customer/booking/payment', views.Cust_Booking_Payment),

    # Common Routes
    path('about_us', views.About_Us),
    path('contact_us', views.Contact_Us),

]
