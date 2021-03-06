from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

from django.db.utils import IntegrityError


class UserView(APIView):

    def get(self, request, **kwargs):
        users = User.objects.get(id=kwargs.get('id'))
        queryset = UsersSerializer(users)
        return Response({'users': queryset.data})

    def post(self, request):
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            password = request.data.get('password')
            user_type = request.data.get('user_type')
            user = User.objects.create(email=email, password=password, user_type=user_type, name=name)
            user.save()
            return Response({'user_id': UsersSerializer(user).data}, status=200)
        except IntegrityError:
            return Response({'msg': 'email field must be unique'}, status=400)

    def delete(self, request, **kwargs):
        try:
            user = User.objects.get(id=kwargs.get('id'))
            user.delete()
            return Response({'msg': 'deleted'}, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'not founded'}, status=404)

    def put(self, request, **kwargs):
        pass
            