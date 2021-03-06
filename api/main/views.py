from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth.models import User


class UserView(APIView):

    def get(self, request):
        users = User.objects.all()
        queryset = UsersSerializer(users, many=True)
        return Response({'users': queryset.data})

    def post(self, request):
        return Response({'s':'s'})