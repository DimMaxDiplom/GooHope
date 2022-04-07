from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from friends.models import Friends
from .models import User, Society


class UserViewSet(mixins.RetrieveModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()

    @staticmethod
    def visibility_regulator(user: User.objects, profile: User.objects) -> bool:
        """
        :param user: Current user
        :param profile: Opened profile
        :return: Profile status (hidden or visible)
        """
        hidden = False
        if not profile.first().publicity == User.publicity_choices[0][0]:
            profile_friends = profile.first().friend.all()
            hidden = True
            if profile_friends:
                # Friend and friends of friends
                if profile.first().publicity == User.publicity_choices[1][0]:
                    if not Friends.contains_friend(profile.first(), user):
                        if [x for x in [Friends.contains_friend(user, x.user) for x in profile_friends if x] if x]:
                            hidden = False
                    else:
                        hidden = False

                # Just friends
                elif profile.first().publicity == User.publicity_choices[2][0]:
                    if Friends.contains_friend(profile.first(), user):
                        hidden = False
        return hidden

    def retrieve(self, request, *args, **kwargs):
        # TODO: доставать id из токена (он будет получен после авторизации)
        _id = kwargs.get('pk')

        user = User.objects.get(id=settings.USER_ID)
        profile = self.queryset.filter(id=_id)

        return Response({
            'user': profile.values('avatar', 'login', 'status', 'description').first(),
            'hidden': UserViewSet.visibility_regulator(user, profile),
            'friends': User.objects.filter(user_id__in=profile.first().friend.all().values('user_id')).values(),
            'societies': Society.objects.filter(societymembers__user=profile.first()).values()
        }, status=status.HTTP_200_OK)
