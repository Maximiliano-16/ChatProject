from django.urls import path

from . import views

app_name = 'MainChat'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # path('', views.home_page, name='home'),
    path('<str:room_name>/<str:username>/', views.message_view, name='room'),
]