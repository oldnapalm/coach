from django.conf.urls import patterns, include, url
from coach.settings import MEDIA_ROOT
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^/?', include('run.urls')),
  url(r'^user/', include('users.urls')),

  url(r'^admin/', include(admin.site.urls)),

  # Medias for dev
  (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
