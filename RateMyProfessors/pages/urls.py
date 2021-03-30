from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('universities/', views.universities, name='universities'),
]