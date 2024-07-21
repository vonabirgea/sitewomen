from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

class MyClass:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b


def index(request):  # HttpRequest
    # t = render_to_string('women/index.html')  # две эти строчки делают то же самое, что и одна строчка сразу под ними
    # return HttpResponse(t)
    data = {
        'titile': 'Главная страница??',
        'main_titile': "Заголовок",
        'menu': menu,
        'float': 28.56,
        'integer': 6,
        'lst': [1, 2, 'abc', True],
        'set': {1, 2, 3, 2, 5},
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass(10, 20),
        'url': slugify("hey hou Lets GOU")
        }
    return render(request, "women/index.html", context=data)


def about(request):
    data = {'titile': 'О сайте'}
    return render(request, "women/about.html", data)


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2024:
        uri = reverse("cats", args=("sport",))
        return HttpResponseRedirect(uri)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):

    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
