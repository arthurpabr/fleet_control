from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^usecontrol/add/$', views.usecontrol_add, name='usecontrol_add'),
    url(r'^usecontrol/list/$', views.usecontrol_list, name='usecontrol_list'),
    url(r'^$', views.index, name='index'),
]
