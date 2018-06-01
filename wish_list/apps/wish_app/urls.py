from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^wishpage$', views.wishpage),
    url(r'^wishpage/add$', views.add_wish),
    url(r'^add_item$', views.add_item),
    url(r'^wishpage/items/(?P<user_id>\d+)$', views.item),
    url(r'^join/(?P<item_id>\d+)$', views.join),
    url(r'^delete/(?P<item_id>\d+)$', views.delete),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]