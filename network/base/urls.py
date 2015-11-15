from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from network.base.views import StationAllView

urlpatterns = patterns(
    'network.base.views',
    url(r'^$', 'index', name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='base/about.html'), name='about'),
    url(r'^robots\.txt$', 'robots', name='robots'),
    url(r'^settings_site/$', 'settings_site', name='settings_site'),

    # Observations
    url(r'^observations/$', 'observations_list', name='observations_list'),
    url(r'^observations/(?P<id>[0-9]+)/$', 'observation_view', name='observation_view'),
    url(r'^observations/(?P<id>[0-9]+)/delete/$', 'observation_delete', name='observation_delete'),
    url(r'^observations/new/$', 'observation_new', name='observation_new'),
    url(r'^prediction_windows/(?P<sat_id>[\w.@+-]+)/(?P<start_date>.+)/(?P<end_date>.+)/$',
        'prediction_windows', name='prediction_windows'),

    # Stations
    url(r'^stations/$', 'stations_list', name='stations_list'),
    url(r'^stations/(?P<id>[0-9]+)/$', 'station_view', name='station_view'),
    url(r'^stations/(?P<id>[0-9]+)/delete/$', 'station_delete', name='station_delete'),
    url(r'^stations/edit/$', 'station_edit', name='station_edit'),
    url(r'^stations_all/$', StationAllView.as_view({'get': 'list'}), name='stations_all'),

)
