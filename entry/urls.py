from django.conf.urls import url

from . import views

app_name = 'entry'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'input', views.input, name='vote'),
    url(r'confirm', views.confirm, name='confirm'),
]
