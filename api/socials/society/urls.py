from rest_framework import status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from society.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['publicity', 'status', 'avatar', 'user_id']


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']

    @action(methods=['get'], detail=True, url_path='test', url_name='test')
    def test_fun(self, request, pk=None):
        self.get_extra_actions()
        return Response({'status': 'Hello world'}, status=status.HTTP_200_OK)

