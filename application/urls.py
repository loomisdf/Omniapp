#urls.py for Application
from django.conf.urls import patterns, url
from application import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<app_id>\d+)/$', views.app_detail, name='app_detail'),
    url(r'^app_upload/$', views.app_upload, name='app_upload'),
    url(r'^app_upload_complete/$', views.app_upload_complete, name='app_upload_complete'),
)

