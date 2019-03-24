from django.urls import path
from . import views

urlpatterns = [
    path('view/<year>/<month>/<day>', views.index)
]
