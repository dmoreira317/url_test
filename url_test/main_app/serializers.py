from rest_framework import serializers
from main_app.models import Measure

class ResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    time = serializers.CharField()
