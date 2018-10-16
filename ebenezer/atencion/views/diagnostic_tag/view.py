from ...models.diagnostic_tag import DiagnosticTag
from django_filters import rest_framework as django_filters
from rest_framework import serializers, viewsets

from .serializer import DiagnosticTagSerializer
# from .filters import DiagnosticTagFilter


class DiagnosticTagViewSet(viewsets.ModelViewSet):
    queryset = DiagnosticTag.objects.all()
    serializer_class = DiagnosticTagSerializer
    permission_classes = ()
    filter_backends = (django_filters.DjangoFilterBackend,)
    filter_fields = ('name',)
    # filterset_class = DiagnosticTagFilter
