from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin


handler404 = 'network.base.views.custom_404'
handler500 = 'network.base.views.custom_500'

urlpatterns = patterns(
    '',

    # Base urls
    url(r'^', include('network.base.urls', namespace='base')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('network.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^avatar/', include('avatar.urls')),

    url(r'^api/', include('network.api.urls'))
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^404/$', handler404),
        url(r'^500/$', handler500),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
