from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^reg_process$', views.reg_process),
    url(r'^log_process$', views.log_process),
    url(r'^travels$', views.travels),
    url(r'^travels/add$', views.add_trip),
    url(r'^travels/destination/(?P<dest_id>\d+)$', views.destination),
    url(r'^trip_process$', views.trip_process),
    url(r'^join_process/(?P<loc_id>\d+)$', views.join_process),
    url(r'^logout$', views.logout),
    url(r'^harddel$', views.harddel),
]