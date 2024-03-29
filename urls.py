from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.defaults import patterns, include, url
from persons.views import index
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve'),
    # Examples:
    # url(r'^$', 'jobjar.views.home', name='home'),
    # url(r'^jobjar/', include('jobjar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^person/',include('persons.urls'), name='create'),
    url(r'$^',index, name='index'),
    url(r'^jobs/',include('notes.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
