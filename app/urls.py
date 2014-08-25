from django.conf.urls import patterns, url

from app.routes import views
from app.routes import database

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api/(?P<collection>\w+)/$', database.documents, name='api.documents'),
    url(r'^api/(?P<collection>\w+)/(?P<id>\w+)/$', database.documents, name='api.document'),
)