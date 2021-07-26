from django.shortcuts import render, redirect
from .models import Room, Messages


# Create your views here.
def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'chatRoom.html')


def checkview(request):
    room_name = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room_name).exists():
        return redirect('/' + room_name + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        return redirect('/' + room_name + '/?username=' + username)
