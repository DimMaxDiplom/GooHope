from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from society.models import User


class DialogsViewSet(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        # dialogs = [dialog.dialog for dialog in Dialogs.objects.filter(user_id=settings.USER_ID)]

        # return Response({'dialogs': dialogs}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)