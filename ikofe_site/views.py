from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return render(request, 'index.html')


def not_found(request):
    return render(request, '404.html')
