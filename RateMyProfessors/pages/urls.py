from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('universities/', views.universities, name='universities'),
    path('lecturers/', views.lecturers, name='lecturers'),
    path('university/detail/<id>/', views.university, name='university'),
    path('profile/<id>/', views.profile, name='profile'),
]
