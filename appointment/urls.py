from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('new', views.appointment_new, name='appointment-new'),
    path('<pk>', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('view/', RedirectView.as_view(pattern_name='appointment-table'), name='appointment-default'),
    path('view/<pk>', views.AppointmentDetailView.as_view  (), name='appointment-detail'),
    path('view/<month>/<day>/<year>', views.table, name='appointment-table'),
    path('view/<month>/<day>/<year>/<pk>', views.AppointmentDetailView.as_view(), name='appointment-detail'),
]
