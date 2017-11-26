from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import UserInfo


def index(request):
    print('entry index')
    return render(request, 'entry/index.html', {})


def input(request):
    return render(request, 'entry/input.html', {})


def confirm(request):
    if request.method == 'POST':
        print(request.POST)
        # use Post-Redirect-Get shortcut
        return redirect('entry:confirm')

    return render(request, 'entry/confirm.html', {})
