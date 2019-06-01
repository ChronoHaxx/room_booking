from django.urls import path
from . import views
import datetime

year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day


urlpatterns = [
    path('new', views.appointment_new, name='appointment-new'),
    path('<pk>', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('view/<pk>', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('view/<month>/<day>/<year>', views.table, name='appointment-table'),
    path('view/<month>/<day>/<year>/<pk>', views.AppointmentDetailView.as_view(), name='appointment-detail')
]
