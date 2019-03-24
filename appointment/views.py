from django.shortcuts import render
from appointment.models import room1, room2, room3

def index(request,year,month,day):
    room1new = room1.objects.all().filter(start_time__year=year, 
                                        start_time__month=month, 
                                        start_time__day=day)

    room2new = room2.objects.all().filter(start_time__year=year, 
                                        start_time__month=month, 
                                        start_time__day=day)

    room3new = room3.objects.all().filter(start_time__year=year, 
                                        start_time__month=month, 
                                        start_time__day=day)

    return render(request,'index.html',context={"room1" : room1new,
                                                "room2" : room2new,
                                                "room3" : room3new})

