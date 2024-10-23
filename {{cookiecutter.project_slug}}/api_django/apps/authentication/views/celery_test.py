from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..tasks import add


class CeleryTestView(APIView):

    def get(self, request):
        task_id = add.delay(2, 3)
        return Response(data={'message': f'task_id {task_id}'}, status=status.HTTP_200_OK)
