from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ProfileView(APIView):

    def get(self, request):
        user_data = {
            'id': request.user.id,
            'name': request.user.first_name,
            'avatar': request.user.profile.avatar_url,
        }
        return Response(data={'user': user_data, 'nextState': '/'}, status=status.HTTP_200_OK)
