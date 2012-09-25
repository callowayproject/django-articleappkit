from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

from .models import Story

urlpatterns = patterns('',
    url('^/', ListView.as_view(model=Story)),
    url('^/(?P<slug>[-\w]+)/$', DetailView.as_view(model=Story))
)