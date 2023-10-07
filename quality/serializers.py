from rest_framework import serializers
from .models import ConcentrateQuality

class ConcentrateQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcentrateQuality
        fields = '__all__'
