from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo


def index(request):
    return render(request, 'entry/index.html', {})


def input(request):
    return render(request, 'entry/input.html', {})


def confirm(request):
    print(request)
    print(request.POST)
    return render(request, 'entry/confirm.html', {})
