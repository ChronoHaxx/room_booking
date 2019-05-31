import datetime

from django.shortcuts import render, redirect
from .models import Appointment
from django.core import serializers

from django.utils import timezone
from django.views.generic.detail import DetailView
from django import forms
from .forms import AppointmentForm, MyForm, QuerydateForm
from django.utils import timezone


def index(request,year,month,day):

    appointments = serializers.serialize('json', Appointment.objects.filter(start_time__year=year, 
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

#detail view generic

class AppointmentDetailView(DetailView):

    model = Appointment
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

#forms for appointment
def add_model(request):
 
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
 
    else:
 
        form = AppointmentForm()
 
        return render(request, "form.html", {'form': form})

