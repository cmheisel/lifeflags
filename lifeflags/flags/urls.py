from django.conf.urls.defaults import patterns, url, handler500, handler404

from lifeflags.flags import views

SLUG_RE = '(?P<slug>\w+)/$'

urlpatterns = patterns('',
    url(SLUG_RE, views.show, name='detail_view'),
    url('$', views.index, name="index"),
)
