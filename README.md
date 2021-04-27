### Project for Booking a Movie, built in Django3-Python.

#### This is Mini-version of Book-My-Shows...

## This Demo is in Fast speed, check at bottom for slowed-down speed demo Gif.

![Demo-in-GIF](https://github.com/ganesh-deshmukh/Project-Movie-Ticket-Booking/blob/main/Meta-Data-for-MarkDown/Demo-Python-Project-in-Django3.gif)

1. Project has Two main menus.
    
    1. Admin Panel- To Add, Delete, Update Data as Available Cities, Movies, Theaters, Shows, Seats.
    
    2. Customer Panel- Search for Cities, Movies, Theaters, Shows, Seats, Book.


2. How it works?

    1. Custoemer Registers first, then Logs-in.
    
    2. User is created and assign a group tag as "customer" default.
    
    3. User/Customer Features
        1. Select the City, with autocomplete, just type 1-2 characters and enter, it will show matching cities. eg. type "mum", it shows Mumbai.
        2. Select the Favourite Movie, same with autocompletion
        3. Select Theater
        4. Select Show, as per timings, eg. Morning Show, Afternoon, Evening, Night.
        5. Select your seats, Green Colored are Available and Red ones are Booked/Reserved/UnAvailables.
        6. Book your seat, it will create Booking in backend, with your customer-id.
    

    4. Admin Features
        1. Add City, Movie, Show, Seat and Edit/Update, Delete.
        2. Change availability of Shows and respective available seats for the show.
        3. Choose which Theater shows which movie for which show.


    5. Extras:
        1. User/Customer can't access to Admin menu.
        2. SuperUser is only one for each Database, so
        3. We have Group-based authorization.
        4. Users are added to "customer" group
        5. Theater Staff added to "admin" group
    

    6. Future ToDos/Improvements:
        1. Add Date/Calender, as of now, no option of choosing dates.
        2. Use Redis, for Caching records and faster search autocomplete records, as in-memory db.
        3. Create Documentation
        4. Host on Cloud, with CI/CD Pipeline.

## Please See the working Demo(wait till GIF Loads completely)


![Demo-in-GIF](https://github.com/ganesh-deshmukh/Project-Movie-Ticket-Booking/blob/main/Meta-Data-for-MarkDown/Demo-Python-Project-in-Django3.gif)


![Video-Link](https://github.com/ganesh-deshmukh/Project-Movie-Ticket-Booking/blob/main/Meta-Data-for-MarkDown/Slower-Speed-Demo.gif)


Slower-Speed-Demo.gif