
from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'

class StaticsSerializer(serializers.Serializer):

    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)
    radius = serializers.FloatField(required=True)