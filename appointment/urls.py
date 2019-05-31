from django.urls import path
from . import views

urlpatterns = [
    path('view/<year>/<month>/<day>', views.index, name='appointment-index'),
    path('view/<year>/<month>/<day>/<pk>/', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('new/', views.add_model, name='appointment-new'),
]
