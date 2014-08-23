from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<msg>\d+)/test/$', views.test, name='test')
)