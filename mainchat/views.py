from django.http import JsonResponse
from django.shortcuts import render
from .models import Chat


def chat(request):
    messages = Chat.objects.order_by('-time_create')[:50]
    messages = reversed(messages)

    data = {
        'messages': messages
    }

    return render(request, 'mainchat/home.html', data)


def receive(request):
    name = request.GET.get("name", None)
    message = request.GET.get("message", None)

    if name == "" or message == "":
        response = {
            'alert': 'Заполни все поля'
        }

        return JsonResponse(response)

    else:
        new = Chat(name=name, message=message)
        new.save()

        time = new.time_create

        data = {
            'name': name,
            'message': message,
            'time_create': time,
            'id': new.id
        }

        return render(request, 'mainchat/message.html', data)


def check(request):
    smsid = request.GET.get("sms", None)
    smsid = int(smsid)

    lastsms = Chat.objects.latest("id").id

    if lastsms > smsid:
        newsms = Chat.objects.filter(id__gt=smsid)
        data = {
            'messages': newsms
        }
        return render(request, 'mainchat/messages.html', data)
    else:
        response = {
            'ok': True
        }
        return JsonResponse(response)
