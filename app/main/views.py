from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - главная'
        context['content'] = 'Магазин мебели HOME'
        return context

# def index(request):
#
#     context = {
#         'title': 'Home - главная',
#         'content': 'Магазин мебели HOME',
#     }
#     return render(
#         request,
#         'main/index.html',
#         context
#     )


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - о нас'
        context['content'] = 'О нас'
        context['text_on_page'] = "Наш классный и крутой магазин"
        return context

# def about(request):
#     context = {
#         'title': 'Home - о нас',
#         'content': 'О нас',
#         'text_on_page': "Наш классный и крутой магазин"
#     }
#     return render(
#         request,
#         'main/about.html',
#         context
#     )
# Create your views here.

