# room-booking app for appointments.

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2.1-brightgreen.svg)](https://djangoproject.com)

Base project : https://github.com/ChronoHaxx/counselour-web/blob/master

To do :

-UX (User Experience)
  - [X] Add widget to choose day, forward and back a day
  - [ ] adjust the time to be on working hours 
    -cannot be done due to js script copied is coded exclusively for 24 hour measurement
  - [X] appointment added needed to get approval of Administrator to be displayed on table
    - this includes some form of inbox and outbox for request etc
    - still incomplete because it only blocks the user from changing values from the frontend side
  - [X] add current date display 
  - [ ] bigger text field for objective

-Forms validation of new appointment
  - [ ] so it doesnt allow user to pick date that already booked and approved

-User auth
  - [ ] groups of students, teachers, staff 
  - [ ] this includes the forms to only allow high priveleged group to book 
  - [ ] users profiles.
  

-Design
  - [ ] intuitive field with widget and ordered stuff in appointment-admin
  - [X] simple navigation stuff
  - [ ] retain original table view, too lazy to redesign.
  - [ ] minimalistic modern style 
  - [ ] responsive 
  - [ ] PWA
