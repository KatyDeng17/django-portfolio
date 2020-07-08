from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'jobs/home.html')


def nick(request):
    return render(request, 'jobs/nick.html')
