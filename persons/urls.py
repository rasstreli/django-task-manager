from django.conf.urls.defaults import patterns, url
from persons.views import  create_account

urlpatterns = patterns('',
                url(r'^create_account/$',create_account),
)