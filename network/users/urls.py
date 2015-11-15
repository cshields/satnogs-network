from django.conf.urls import patterns, url

from network.users import views

urlpatterns = patterns(
    'network.users.views',

    url(r'^redirect/$', view=views.UserRedirectView.as_view(), name='redirect_user'),
    url(r'^update/$', view=views.UserUpdateView.as_view(), name='update_user'),
    url(r'^(?P<username>[\w.@+-]+)/$', 'view_user', name='view_user'),
)
