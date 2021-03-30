from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')


def universities(request):
    return render(request, 'pages/universities.html')