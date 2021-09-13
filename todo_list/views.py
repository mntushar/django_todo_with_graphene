from django.shortcuts import HttpResponse
from .models import*


def user_home(request):
    todo = TodoList.objects.filter(userId=2)
    print(todo)
    return HttpResponse('hi')
