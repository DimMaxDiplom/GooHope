from rest_framework import status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from friends.models import Friends
from society.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ['get']

    @staticmethod
    def visibility_regulator(user: User.objects, profile: User.objects) -> bool:
        """
        :param user: Current user
        :param profile: Opened profile
        :return: Profile status (hidden or visible)
        """
        hidden = False
        if not user.first().publicity == User.publicity_choices[0][0]:
            profile_friends = user.first().friend.all()
            hidden = True
            if profile_friends:
                # Friend and friends of friends
                if user.first().publicity == User.publicity_choices[1][0]:
                    if not Friends.contains_friend(user.first(), profile):
                        if [x for x in [Friends.contains_friend(profile, x.user) for x in profile_friends if x] if x]:
                            hidden = False
                    else:
                        hidden = False

                # Just friends
                elif user.first().publicity == User.publicity_choices[2][0]:
                    if Friends.contains_friend(user.first(), profile):
                        hidden = False
        return hidden

    def list(self, request, *args, **kwargs):
        # TODO: доставать id из токена (он будет получен после авторизации)
        TEST_ID = 1
        _id = request.GET.get('id')
        user = self.queryset.filter(id=_id)

        return Response({
            'user': user.values('avatar', 'status', 'description').first(),
            'hidden': UserViewSet.visibility_regulator(user, User.objects.get(id=TEST_ID))
        }, status=status.HTTP_200_OK)
