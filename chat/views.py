from django.shortcuts import render
from .models import Room,Messages

# Create your views here.
def home(request):
    return render(request, 'home.html')


def room(request):
    return


def checkview(request):
    pass
