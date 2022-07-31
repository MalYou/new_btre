from rest_framework import serializers

from .models import Listing
from core.serializers import AddressSerializer
from attachments.serializers import AttachmentsSerializer


class ListingsSerializer(serializers.ModelSerializer):
    """
        Serializer for listing objects
    """

    address = AddressSerializer()
    attachments = AttachmentsSerializer(many=True)

    class Meta:
        model = Listing
        fields = ("title", "price", "address", "sqft", "garage", 
            "bedrooms", "bathrooms", "user", "list_date", "attachments",)


class ListingSerializer(serializers.ModelSerializer):
    """
        Serializer for listing objects
    """

    address = AddressSerializer()
    attachments = AttachmentsSerializer(many=True)

    class Meta:
        model = Listing
        fields = "__all__"
