from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class User(models.Model):
    name = models.CharField(max_length=60)
    id_number = models.CharField(max_length=20, unique=True, primary_key=True)
    department = models.CharField(max_length=30, blank=True)

    STUDENTS = 'S'
    TEACHERS = 'T'
    ADMINS = 'A'
    POSITION_CHOICES = (
        (STUDENTS, 'Students'),
        (TEACHERS, 'Teachers'),
        (ADMINS, 'Admins'),
    )
    position = models.CharField(
    max_length=1,
    choices=POSITION_CHOICES,
    default=STUDENTS,
    )
    


    def __str__(self):
        return self.name


class appointment(models.Model):
    objective = models.CharField(max_length=80)
    start_time = models.DateTimeField(unique=True)
    end_time = models.DateTimeField(unique=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    FAZIL = '1'
    AINUL = '2'
    BILIK = '3'
    ROOM_CHOICES =(
        (FAZIL, 'Cg. Fazilawati'),
        (AINUL, 'Cg Ainul'),
        (BILIK, 'Bilik 3R'),
    )
    rooom = models.CharField(
    max_length=1,
    choices=ROOM_CHOICES,
    default=BILIK,
    )   

    def __str__(self):
        return self.objective
