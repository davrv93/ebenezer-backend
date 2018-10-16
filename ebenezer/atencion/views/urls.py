from django.conf.urls import url, include
from rest_framework import routers
# from .results.view import ResultViewSet
from .diagnostic_tag.view import DiagnosticTagViewSet

router = routers.DefaultRouter()
# router.register(r'results', ResultViewSet)
router.register(r'diagnostic_tags', DiagnosticTagViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
