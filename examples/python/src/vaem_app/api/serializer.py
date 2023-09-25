from rest_framework import serializers
from .models import Status, VaemState

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class VaemStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaemState
        fields = '__all__'
