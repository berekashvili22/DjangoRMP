from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('universities/', views.universities, name='universities'),
    path('lecturers/', views.lecturers, name='lecturers'),
    path('university/detail/<id>/', views.university, name='university'),
    path('lecturer/detail/<id>/', views.lecturer, name='lecturer'),
    path('profile/<id>/', views.profile, name='profile'),
    path('uni-review/del/<id>/', views.deleteUniReview, name='del-uni-review'),
    path('lec-review/del/<id>/', views.deleteLecReview, name='del-lec-review'),
    path('rmp-search/', views.homeSearch, name='homeSearch'),
    
]
