from django.conf.urls import patterns, url

from about_us import views

urlpatterns = patterns('',
    url(r'^$', views.about, name='about_us'),
)