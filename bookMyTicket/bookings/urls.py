from django.urls import path
from . import views
from . import formViews

urlpatterns = [
    # 1. Admin Routes 
    
    # 1.1 for Listing
    path('theater_admin/home', views.Admin_Home),
    path('theater_admin/list/city', views.Admin_List_City),
    path('theater_admin/list/movie', views.Admin_List_Movie),
    path('theater_admin/list/theater', views.Admin_List_Theater),
    path('theater_admin/list/shows/<str:theater_id>/', views.Admin_List_Shows),
    path('theater_admin/list/seats/<str:show_id>/', views.Admin_List_Seats),
    path('theater_admin/seats/details/<str:seat_id>/', views.Admin_Seat_Details),

    # 1.2 for Updating values
    path('theater_admin/create/city', formViews.Create_City_Form),
    path('theater_admin/create/movie', formViews.Create_Movie_Form),
    path('theater_admin/create/theater', formViews.Create_Theater_Form),
    path('theater_admin/create/shows/<str:theater_id>/', formViews.Create_Shows_Form),
    path('theater_admin/create/seats/<str:show_id>/', formViews.Create_Seats_Form),

    # 2. Customer Routes
    path('', views.Cust_Home_Book_Now),
    path('customer/select/city', views.Cust_Select_City),
    path('customer/select/movie', views.Cust_Select_Movie),
    path('customer/select/theater', views.Cust_Select_Theater),
    path('customer/select/show', views.Cust_Select_Show),
    path('customer/select/seat', views.Cust_Select_Seat),
    path('customer/booking/payment', views.Cust_Booking_Payment),

    # 3. Common Routes
    path('about_us', views.About_Us),
    path('contact_us', views.Contact_Us),

]
