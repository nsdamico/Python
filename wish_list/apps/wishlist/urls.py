from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^main$', views.index),
    url(r'^process/(?P<action>\w+)$', views.process),    
    url(r'^dashboard$', views.wishes),
    url(r'^wish_items/create$', views.create),
    url(r'^add_process$', views.add_process),
    url(r'^remove/(?P<wish_id>\d+)$', views.remove),
    url(r'^delete/(?P<wish_id>\d+)$', views.delete),
    url(r'^join/(?P<wish_id>\d+)$', views.join_wish),
    url(r'^wish_items/(?P<wish_id>\d+)$', views.item),
    url(r'^logout$', views.logout),


]