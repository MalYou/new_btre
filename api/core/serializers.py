from rest_framework import serializers

from . import models


class CountrySerializer(serializers.ModelSerializer):
    """
        Serializer for country objects
    """

    class Meta:
        model = models.Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    """
        Serializer for country objects
    """
    country = CountrySerializer()

    class Meta:
        model = models.State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    """
        Serializer for country objects
    """

    class Meta:
        model = models.City
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    """
        Serializer for country objects
    """

    class Meta:
        model = models.Address
        fields = '__all__'
