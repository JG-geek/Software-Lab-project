from django.urls import path
from . import views

urlpatterns = [
    path('yearWiseComparison/', views.yearWiseComparison, name="yearWiseComparison"),
]