from django.shortcuts import render
from .models import appointment
from django.core import serializers

def index(request,year,month,day):
    #appointments = appointment.objects.all().filter(start_time__year=year, 
    #                                                start_time__month=month, 
    #                                                start_time__day=day)
    appointments = serializers.serialize('json', appointment.objects.filter(start_time__year=year, 
                                                            start_time__month=month, 
                                                            start_time__day=day),
                                                        fields=('objective', 
                                                                'start_time', 
                                                                'end_time',
                                                                'client',
                                                                'rooom'))    

    #to get duration in minute
    #durations = []
    #for x in appointments :
    #    duration = x.end_time - x.start_time
    #    duration_array = str(duration).split(':')
    #    duration_minute = (int(duration_array[0]) * 60) + int(duration_array[1])
    #    durations.append(duration_minute)

    return render(request,'index.html',context={"appointments" : appointments,
                                                #"durations" : durations,
                                                })

