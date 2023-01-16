from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

User = get_user_model()


class Room(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    room_name = models.CharField(max_length=255)
    members = models.ManyToManyField(
        User,
        related_name='users_in_room',
        verbose_name='Участники_беседы'
    )

    def __str__(self):
        return self.room_name


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    def __str__(self):
        return str(self.room)
