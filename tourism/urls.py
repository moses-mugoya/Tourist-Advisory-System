from django.urls import re_path
from . import views

app_name = 'tourism'

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path('^destinations/', views.destination, name='destination'),
    re_path('^suggestions/', views.question, name='suggestion'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.detail, name='detail'),
    re_path(r'^(?P<id>\d+)/$', views.get_expense, name='expense'),
]

