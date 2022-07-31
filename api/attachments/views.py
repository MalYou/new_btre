from rest_framework import generics
from rest_framework.response import Response

from .models import Attachment
from .serializers import AttachmentsSerializer

class AttachmentView(generics.RetrieveAPIView):
    """
        View to retrieve Listing attachments
    """

    serializer_class = AttachmentsSerializer
    queryset = Attachment.objects.all()

    def get(self, request, *args, **kwargs):
        attachment = self.get_object()
        serialized_attachment = AttachmentsSerializer(attachment)

        return Response(serialized_attachment.data)
