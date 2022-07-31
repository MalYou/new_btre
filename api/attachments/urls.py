from django.urls import path

from .views import AttachmentView


urlpatterns = [
    path("<str:pk>", view=AttachmentView.as_view(), name="attachment-details")
]
