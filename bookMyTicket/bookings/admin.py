from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(City)
admin.site.register(Theater)
admin.site.register(Movie)
admin.site.register(Shows)
admin.site.register(Seats)
admin.site.register(Booking)
admin.site.register(ShowsFromTheater)