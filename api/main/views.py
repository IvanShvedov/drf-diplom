from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class UserView(APIView):

    def get(self, request):
        users = User.objects.all()
        queryset = UsersSerializer(users, many=True)
        return Response({'users': queryset.data})

    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        user_type = request.data.get('user_type')
        user = User.objects.create(email=email, password=password, user_type=user_type, name=name)
        user.save()
        return Response({'user_id': user.pk}, status=200)