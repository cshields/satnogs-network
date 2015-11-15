from rest_framework import routers
from network.api import views


router = routers.DefaultRouter()

router.register(r'jobs', views.JobView, base_name='jobs')
router.register(r'data', views.DataView, base_name='data')

urlpatterns = router.urls
