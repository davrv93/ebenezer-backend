import django_filters

from django_filters import rest_framework as filters

from ...models.diagnostic_tag import DiagnosticTag


class DiagnosticTagFilter(django_filters.FilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup='icontains'
    )

    class Meta:
        model = DiagnosticTag
        fields = ('name')
