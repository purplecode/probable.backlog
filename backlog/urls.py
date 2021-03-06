from django.conf.urls import patterns, url

from backlog.routes import views
from backlog.routes import database

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api/(?P<collection>\w+)$', database.documents, name='api.documents'),
    url(r'^api/(?P<collection>\w+)/(?P<id>\w+)$', database.document, name='api.document'),
)
