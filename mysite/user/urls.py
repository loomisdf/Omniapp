from django.conf.urls import patterns, url
from user import views

urlpatterns = patterns('',
    url(r'^$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
)
