import datetime
from django.views import View
from django.shortcuts import render, redirect
from .models import Appointment
from django.core import serializers
from django.utils import timezone
from django.views.generic.detail import DetailView
from django import forms, urls
from .forms import AppointmentForm

date_today = datetime.date.today()
year_today = str(date_today.year)
month_today = str(date_today.month)
day_today = str(date_today.day)

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
            return redirect('/appointment/view/' + month_today + '/' + day_today + '/' + year_today)
    else:
        form = AppointmentForm()
    return render(request, "form.html", {'form': form})