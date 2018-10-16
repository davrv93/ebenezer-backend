from ...models.diagnostic_tag import DiagnosticTag
from rest_framework import serializers, viewsets

# Serializers define the API representation.


class DiagnosticTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticTag
        fields = '__all__'
