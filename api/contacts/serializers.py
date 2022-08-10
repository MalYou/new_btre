from attr import field
from rest_framework import serializers

from .models import Contact

class ContactsSerializer(serializers.ModelSerializer):
    """
        Serializer for contacts objects
    """

    class Meta:
        model = Contact
        fields = "__all__"
