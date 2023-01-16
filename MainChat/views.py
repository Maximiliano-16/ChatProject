from django.shortcuts import get_object_or_404, redirect, render

from .models import Room, Message


def index(request):
    if request.method == 'POST':
        room = request.POST['room']
        username = request.user
        try:
            get_room = Room.objects.get(room_name=room)
            # get_room.members.set(username)
            return redirect('room', room_name=room, username=username)

        except Room.DoesNotExist:
            new_room = Room(room_name=room, members=request.user)
            new_room.save()
            return redirect('room', room_name=room, username=username)
    context = {

    }
    return render(request, 'MainChat/index.html', context)


# def home_page(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         room = request.POST['room']
#
#         try:
#             get_room = Room.objects.get(room_name=room)
#             return redirect('room', room_name=room, username=username)
#
#         except Room.DoesNotExist:
#             new_room = Room(room_name=room)
#             new_room.save()
#             return redirect('room', room_name=room, username=username)
#
#     return render(request, 'MainChat/index.html')


def message_view(request, room_name, username):
    get_room = get_object_or_404(Room, room_name=room_name)
    # get_room = Room.objects.get(room_name=room_name)

    if request.method == 'POST':
        message = request.POST['message']

        print(message)

        new_message = Message(room=get_room, sender=username, message=message)
        new_message.save()

    get_messages = Message.objects.filter(room=get_room)

    context = {
        "messages": get_messages,
        "user": username
    }
    return render(request, 'message.html', context)
