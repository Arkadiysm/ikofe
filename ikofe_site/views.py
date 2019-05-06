from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Project, Event
from .forms import IkofeForm, form_handler


def index(request):
    was_mail_sent = False
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            was_mail_sent = True
    events = Event.get_last_events(6)
    context = {
        'events': events,
        'title': 'Главная',
        'form': IkofeForm(),
        'wasMailSent': was_mail_sent
    }
    return render(request, 'index.html', context=context)


def elevator(request):
    was_mail_sent = False
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            was_mail_sent = True
    context = {
        'title': 'Реклама в лифтах',
        'form': IkofeForm(),
        'wasMailSent': was_mail_sent
    }
    return render(request, 'elevator.html', context=context)


def video_advertising(request):
    was_mail_sent = False
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            was_mail_sent = True
    projects = Project.get_last_projects(6)
    context = {
        'title': 'Видеореклама',
        'form': IkofeForm(),
        'projects': projects,
        'wasMailSent': was_mail_sent
    }
    return render(request, 'video_ad.html', context=context)


def event(request, value=1):
    was_mail_sent = False
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            was_mail_sent = True
    events_quantity = Event.get_events_quantity()
    pages_quantity = events_quantity / 8 if events_quantity % 8 == 0 \
        else events_quantity // 8 + 1

    context = {
        'title': 'Новости',
        'events': Event.get_last_events(value*8, start_from=value*8-7),
        'pages_quantity': range(1, int(pages_quantity)+1),
        'form': IkofeForm(),
        'wasMailSent': was_mail_sent
    }

    if context['events']:
        return render(request, 'event.html', context=context)
    else:
        return not_found(request)


def project(request, category='all'):
    was_mail_sent = False
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            was_mail_sent = True
    projects = Project.get_all() if category == 'all' \
        else Project.get_all_by_category(category)

    context = {
        'title': 'Проекты',
        'projects': projects,
        'form': IkofeForm,
        'wasMailSent': was_mail_sent
    }

    if context['projects'] != None:
        return render(request, 'project.html', context=context)
    else:
        return not_found(request)


def contacts(request):
    was_mail_sent = False
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            was_mail_sent = True
    context = {
        'title': 'Контакты',
        'form': IkofeForm,
        'wasMailSent': was_mail_sent
    }
    return render(request, 'contacts.html', context=context)


def project_articles(request, value):
    was_mail_sent = False
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            was_mail_sent = True

    events = Event.get_last_events(6)
    article = Project.get_project_by_id(value)
    context = {
        'title': 'Проекты',
        'article': article,
        'events': events,
        'form': IkofeForm,
        'wasMailSent': was_mail_sent
    }
    if context['article']:
        return render(request, 'articles.html', context=context)
    else:
        return not_found(request)


def event_articles(request, value):
    was_mail_sent = False
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            was_mail_sent = True

    events = Event.get_last_events(6)
    article = Event.get_event_by_id(value)
    context = {
        'title': 'Новости',
        'article': article,
        'events': events,
        'form': IkofeForm,
        'wasMailSent': was_mail_sent
    }
    if context['article']:
        return render(request, 'articles.html', context=context)
    else:
        return not_found(request)


def about_us(request):
    was_mail_sent = False
    if request.method == 'POST':
        if form_handler(request, IkofeForm):
            was_mail_sent = True

    context = {
        'title': 'О нас',
        'form': IkofeForm,
        'wasMailSent': was_mail_sent
    }

    return render(request, 'about_us.html', context=context)


def not_found(request):
    return render(request, '404.html')


