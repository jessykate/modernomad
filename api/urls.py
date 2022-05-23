from django.urls import include, re_path

from rest_framework import routers
from api.views.capacities import capacities, capacity_detail
import rest_framework.urls

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^capacities/$', capacities),
    re_path(r'^capacity/(?P<capacity_id>[0-9]+)$', capacity_detail),
    re_path(r'^api-auth/', include(rest_framework.urls, namespace='rest_framework')),
]
