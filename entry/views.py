from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    test ="ak"
    return render(request, 'entry/index.html', {})


def input(request):
    return render(request, 'entry/input.html', {})


def confirm(request):
    return render(request, 'entry/confirm.html', {})
