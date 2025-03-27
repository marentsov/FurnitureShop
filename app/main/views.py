from django.shortcuts import render


def index(request):

    context = {
        'title': 'Home - главная',
        'content': 'Магазин мебели HOME',
    }
    return render(
        request,
        'main/index.html',
        context
    )


def about(request):
    context = {
        'title': 'Home - о нас',
        'content': 'О нас',
        'text_on_page': "Наш классный и крутой магазин"
    }
    return render(
        request,
        'main/about.html',
        context
    )
# Create your views here.

