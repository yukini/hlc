from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from django.utils import timezone

from .models import UserInfo
from .forms import UserInfoForm


def index(request):
    print('entry index')
    return render(request, 'entry/index.html', {})


class UserInfoCreateView(CreateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = "entry/input.html"

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        print("debug です")
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' バリデーションに失敗した時 '''
        print("debug invalid です")
        return super().form_invalid(form)


def input(request):
    return render(request, 'entry/input.html', {})


def confirm(request):
    if request.method == 'POST':
        print(request.POST)
        # use Post-Redirect-Get shortcut
        return redirect('entry:confirm')

    return render(request, 'entry/confirm.html', {})
