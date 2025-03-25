from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница сайта',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authen': True,
    }
    return render(
        request,
        'main/index.html',
        context
    )


def about(request):
    return HttpResponse('About page')
# Create your views here.

