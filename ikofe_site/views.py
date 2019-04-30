from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Project, Event
from .forms import IkofeForm, form_handler


def index(request):
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            pass
    events = Event.get_last_events(6)
    context = {
        'events': events,
        'title': 'Главная',
        'form': IkofeForm(),
    }
    return render(request, 'index.html', context=context)


def elevator(request):
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            pass
    context = {
        'title': 'Реклама в лифтах',
        'form': IkofeForm(),
    }
    return render(request, 'elevator.html', context=context)


def video_advertising(request):
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            pass
    projects = Project.get_last_projects(6)
    context = {
        'title': 'Видео реклама',
        'form': IkofeForm(),
        'projects': projects,
    }
    return render(request, 'video_ad.html', context=context)


def event(request, value=1):
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            pass
    events_quantity = Event.get_events_quantity()
    pages_quantity = events_quantity / 8 if events_quantity % 8 == 0 \
        else events_quantity // 8 + 1

    context = {
        'title': 'Новости',
        'events': Event.get_last_events(value*8, start_from=value*8-7),
        'pages_quantity': range(1, pages_quantity+1),
        'form': IkofeForm(),
    }

    if context['events']:
        return render(request, 'event.html', context=context)
    else:
        return not_found(request)


def project(request, category='all'):
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            pass
    projects = Project.get_all() if category == 'all' \
        else Project.get_all_by_category(category)

    context = {
        'title': 'Проекты',
        'projects': projects,
        'form': IkofeForm,
    }

    if context['projects'] != None:
        return render(request, 'project.html', context=context)
    else:
        return not_found(request)


def contacts(request):
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            pass
    context = {
        'title': 'Контакты',
        'form': IkofeForm
    }
    return render(request, 'contacts.html', context=context)


def project_articles(request, value):
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            pass

    events = Event.get_last_events(6)
    article = Project.get_project_by_id(value)
    context = {
        'title': 'Проекты',
        'article': article,
        'events': events,
        'form': IkofeForm,
    }
    if context['article']:
        return render(request, 'articles.html', context=context)
    else:
        return not_found(request)


def event_articles(request, value):
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            pass

    events = Event.get_last_events(6)
    article = Event.get_event_by_id(value)
    context = {
        'title': 'Новости',
        'article': article,
        'events': events,
        'form': IkofeForm,
    }
    if context['article']:
        return render(request, 'articles.html', context=context)
    else:
        return not_found(request)


def not_found(request):
    return render(request, '404.html')


