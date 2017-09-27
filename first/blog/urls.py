from django.conf.urls import include, url
from .views import index, list, detail

urlpatterns = [
    url(r'^$', index, name='blog'),

    url(r'^ko/(?P<tag_tag>\w.*)/$', list, name='list'),

    url(r'^ko/article/(?P<a_id>\d.*)/$', detail, name='detail'),
]