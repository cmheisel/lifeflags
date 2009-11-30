from django.conf.urls.defaults import patterns, url

from flags import views

SLUG_RE = '(?P<slug>\w+)$'

urlpatterns = patterns('',
    url(SLUG_RE, views.show), 
)
