from django.urls import path
from . import views

urlpatterns = [
    path('number_classifier/', views.number_classifier, name='number_classifier'),
]
