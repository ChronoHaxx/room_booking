import datetime

from django.shortcuts import render, redirect
from .models import Appointment
from django.core import serializers
from django.utils import timezone
from django.views.generic.detail import DetailView
from django import forms, urls
from .forms import AppointmentForm

#find current date
year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day

#default would go to todays date
def index(request, year=year, month=month, day=day):

    appointments = serializers.serialize('json', Appointment.objects.filter(start_time__year=year, 
                                                            start_time__month=month, 
                                                            start_time__day=day),
                                                        fields=('objective', 
                                                                'start_time', 
                                                                'end_time',
                                                                'client',
                                                                'rooom'))    

    return render(request,'index.html',context={"appointments" : appointments,
                                                })

def table(request, year, month, day):

    appointments = serializers.serialize('json', Appointment.objects.filter(start_time__year=year, 
                                                            start_time__month=month, 
                                                            start_time__day=day),
                                                        fields=('objective', 
                                                                'start_time', 
                                                                'end_time',
                                                                'client',
                                                                'rooom'))    

    return render(request,'table.html',context={"appointments" : appointments,
                                                })


#detail view generic
class AppointmentDetailView(DetailView):

    model = Appointment
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

#forms for appointment
def appointment_new(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.User = request.user
            appointment.save()
            return redirect(urls.reverse(index))
    else:
        form = AppointmentForm()
    return render(request, "form.html", {'form': form})

def test(request):
    return render(request, "test.html")