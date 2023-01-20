## Chat_project
____
## Цель работы:
Разработать и реализовать анонимный чат с возможностью создания каналов. Сообщения доставляются пользователю без обновления страницы.
## Реализованные возможности
+ Применена технология AJAX
+ Создание каналов для чатов
+ Возможность подключения к уже существующему каналу
+ Автоматическое удаление сообщений через заданный интервал времени
+ Автоматическое удаление старых каналов 
____
## Ход работы
### 1. Разработка пользовательского интерфейса
В ходе выполнения работы был разработан пользовательский интерфейс при помощи графического редактора [Figma](https://www.figma.com/community)
![login](https://user-images.githubusercontent.com/98755619/212743893-db3e8172-34af-42ba-bd29-508999045220.png)
![index](https://user-images.githubusercontent.com/98755619/212744105-399600d8-0f90-45bf-b852-6036f868bce7.png)
![chat](https://user-images.githubusercontent.com/98755619/212744124-92aae008-91b8-4525-8b45-06741b5eef4a.png)

### 2. Описание пользовательских сценариев работы
1) Пользователь заходит на сайт и попадает на страничку, где ему надо ввести свой никнейм на сайте.
2) После ввода никнейма становится доступна глпвная страница сайта, где можно найти или создать чат, а также отображаются все чаты, в которых состоит пользователь.
3) Клиент может открыть чат, в котором состоит, и начать общаться, а при желании может выйти из чата.

### 3. Описание API сервера и хореографии
![диаграмма](https://user-images.githubusercontent.com/98755619/213705573-38a38835-3cb7-45e6-9283-82926910c0cf.png)

### 4. Описание структура базы данных
![bd](https://user-images.githubusercontent.com/98755619/212910219-808d8b14-4b17-4a3b-959e-19ce7841b0e0.png)

### 5. Алгоритмы
![diagram login](https://user-images.githubusercontent.com/98755619/212920271-ce4844c5-905c-4d23-b219-0ad215e116ed.png)
![main drawio](https://user-images.githubusercontent.com/98755619/212920309-0cb17b63-30a9-4246-887f-680197b858a9.png)
![chat drawio](https://user-images.githubusercontent.com/98755619/212920349-89f2a422-8798-4ed5-a428-385b8bb7523f.png)


### 6. Значимые части кода

Код моделей:
```
class Room(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    room_name = models.CharField(max_length=255)
    members = models.ManyToManyField(
        User,
        related_name='users_in_room',
        verbose_name='Участники_беседы',
        blank=True
    )

    def __str__(self):
        return self.room_name


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='messages',
        blank=True
    )
```

Функция создания комнат:
```
def index(request):
    if request.method == 'POST':
        room = request.POST['room']
        username = request.user.username
        if Room.objects.filter(room_name=room).exists():
            new_room = Room.objects.get(room_name=room)
            new_room.members.add(request.user)
            return redirect('MainChat:room', room_name=room, username=username)
        new_room = Room.objects.create(room_name=room)
        new_room.members.add(request.user)
        return redirect('MainChat:room', room_name=new_room.room_name,
                        username=username)

    context = {

    }
    return render(request, 'MainChat/index.html', context)
```

JS функции для вывода сообщений
```
$(document).on('submit', '#message', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: "",
        data: {
            message: $('#msg').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        }
    });
    $( ".parent" ).load(window.location.href + " .parent" );
})

$(document).ready(function(){
    setInterval(function(){
        $( ".message" ).load(window.location.href + " .message" );
    }, 10000)
})
```
