from rest_framework.views import APIView
from rest_framework.response import Response

from main.models import User

class VacancyResponseView(APIView):

    def get(self, request):
        return Response()

    


class CvResponseView(APIView):

    def get(self, request):
        return Response("a")