from django.conf.urls import patterns, url, include
from rest_framework import routers

from network.api import views


router = routers.DefaultRouter()

router.register(r'data', views.DataView)
router.register(r'jobs', views.JobView)


urlpatterns = patterns(
    '',
    url(r'^', include(router.urls))
)
