from django.conf.urls import url
from . import views
from .views import VehicleCreate, VehicleUpdate, VehicleDelete, \
                VehicleListView, VehicleDetailView


urlpatterns = [
    url(r'^vehicle/add/$', VehicleCreate.as_view() , name='vehicle_add'),
    url(r'^vehicle/(?P<pk>\d+)/$', VehicleUpdate.as_view() , name='vehicle_update'),
    url(r'^vehicle/(?P<pk>\d+)/delete/$', VehicleDelete.as_view() , name='vehicle_delete'),
    url(r'^vehicle_view/(?P<pk>\d+)$', VehicleDetailView.as_view() , name='vehicle_detail'),
    url(r'^vehicle/list/$', VehicleListView.as_view(), name='vehicle_list'),
    url(r'^usecontrol/add/$', views.usecontrol_add, name='usecontrol_add'),
    url(r'^usecontrol/list/$', views.UseControlListView.as_view(), name='usecontrol_list'),
    url(r'^$', views.index, name='index'),
]
