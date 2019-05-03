from django.urls import re_path
from . import views

app_name = 'account'

urlpatterns = [
    re_path(r'^$', views.dashboard, name='dashboard'),
    re_path(r'^expense/(?P<id>\d+)/$', views.expense, name='expend'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^edit/$', views.edit, name='edit'),

]
