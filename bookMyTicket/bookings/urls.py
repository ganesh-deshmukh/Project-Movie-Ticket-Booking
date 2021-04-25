from django.urls import path
from . import views
from . import formViews

urlpatterns = [
    # 1. Admin Routes 
    
    # 1.1 for Listing
    path('theater_admin/home', views.Admin_Home),
    path('theater_admin/list/city', views.Admin_List_City, name="list_cities"),
    path('theater_admin/list/movie', views.Admin_List_Movie, name="list_movies"),
    path('theater_admin/list/theater', views.Admin_List_Theater, name="list_theaters"),
    path('theater_admin/list/shows/<str:theater_id>/', views.Admin_List_Shows, name="list_shows"),
    path('theater_admin/list/seats/<str:show_id>/', views.Admin_List_Seats, name="list_seats"),
    path('theater_admin/seats/details/<str:seat_id>/', views.Admin_Seat_Details, name="list_seat_details"),

    # City
    path('theater_admin/create/city', formViews.Create_City_Form, name="create_city"),
    path('theater_admin/update/city/<str:city_id>/', formViews.Update_City_Form, name="update_city"),
    path('theater_admin/delete/city/<str:city_id>/', formViews.Delete_City_Form, name="delete_city"),


    # Movie
    path('theater_admin/create/movie', formViews.Create_Movie_Form, name="create_movie"),
    path('theater_admin/update/movie/<str:movie_id>/', formViews.Update_Movie_Form, name="update_movie"),
    path('theater_admin/delete/movie/<str:movie_id>/', formViews.Delete_Movie_Form, name="delete_movie"),



    # Theater
    path('theater_admin/create/theater', formViews.Create_Theater_Form, name="create_theater"),
    path('theater_admin/update/theater/<str:theater_id>/', formViews.Update_Theater_Form, name="update_theater"),
    path('theater_admin/delete/theater/<str:theater_id>/', formViews.Delete_Theater_Form, name="delete_theater"),



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
