from rest_framework import serializers

from .models import Listing
from core.serializers import AddressSerializer


class ListingSerializer(serializers.ModelSerializer):
    """
        Serializer for listing objects
    """
    address = AddressSerializer()

    class Meta:
        model = Listing
        exclude = ("user",)
