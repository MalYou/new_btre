from rest_framework import serializers

from . import models

class AttachmentsSerializer(serializers.ModelSerializer):
    """
        Serializer for attachment objects
    """

    class Meta:
        model = models.Attachment
        fields = "__all__"
