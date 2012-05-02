__author__ = 'pavel'
from django.conf.urls.defaults import patterns, include, url
from notes.views import create_job, job, job_list
from django.conf.urls.defaults import patterns, url
urlpatterns = patterns('',
    url(r'^create/',create_job),
    url(r'^$', job_list),
    url(r'^joblist/(?P<job_id>\d+)',job),
)
