from django.shortcuts import render, redirect

from .forms import EntryUserForm


def index(request):
    return render(request, 'entry/index.html', {})


def input(request):
    form_data = request.session.get("form_data", None)
    form = EntryUserForm(form_data)
    context = {
        "form": form,
    }
    return render(request, 'entry/input.html', context)


def confirm(request):
    form_data = request.session.get("form_data", None)
    '''確認画面へ'''
    if request.method == 'POST':
        form = EntryUserForm(request.POST)
        if form.is_valid():
            request.session['form_data'] = request.POST
        # use Post-Redirect-Get shortcut
        else:
            print(form.errors)
            pass
        return redirect('entry:confirm')

    return render(request, 'entry/confirm.html', {"form": form_data})


def complete(request):
    form_data = request.session.pop("form_data", None)
    '''完了画面へ'''
    if request.method == 'POST':
        form = EntryUserForm(form_data)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        # use Post-Redirect-Get shortcut
        return redirect('entry:complete')

    return render(request, 'entry/complete.html', {})
