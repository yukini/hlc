from django.conf.urls import url

from . import views
from .views import UserInfoCreateView

app_name = 'entry'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'input', UserInfoCreateView.as_view, name='input'),
    url(r'input', UserInfoCreateView.as_view()),
    url(r'confirm', views.confirm, name='confirm'),
]
