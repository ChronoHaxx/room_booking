from django.shortcuts import render
from .models import appointment


def index(request,year,month,day):
    appointments = appointment.objects.all().filter(start_time__year=year, 
                                        start_time__month=month, 
                                        start_time__day=day)

    return render(request,'index.html',context={"appointments" : appointments
                                                })

