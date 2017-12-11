from django.conf.urls import url

from . import views

app_name = 'entry'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'input', UserInfoCreateView.as_view, name='input'),
    url(r'input', views.input, name='input'),
    url(r'confirm', views.confirm, name='confirm'),
    url(r'complete', views.complete, name='complete'),
]
