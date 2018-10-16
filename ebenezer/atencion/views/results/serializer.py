from ..models.results import Result
from rest_framework import serializers, viewsets

# Serializers define the API representation.


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
