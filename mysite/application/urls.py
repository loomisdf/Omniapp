from django.conf.urls import patterns, url
from application import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<app_id>\d+)/$', views.app_detail, name='app_detail'),
)

