from django.urls import path
from . import views

urlpatterns = [
    path('new', views.appointment_new, name='appointment-new'),
    path('view', views.index, name='appointment-index'),
    path('view/<pk>/', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('view/<year>/<month>/<day>', views.table, name='appointment-table'),
    path('view/<year>/<month>/<day>/<pk>/', views.AppointmentDetailView.as_view(), name='appointment-detail')
]
