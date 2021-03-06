from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import IntegrityError

import json

from .utils import *
from .models import *
from .serializers import *



class UserView(APIView):

    def get(self, request, **kwargs):
        users = User.objects.get(id=kwargs.get('id'))
        queryset = UsersSerializer(users)
        return Response({'users': queryset.data}, status=status.status.HTTP_200_OK)

    def post(self, request):
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            password = request.data.get('password')
            user_type = request.data.get('user_type')
            user = User.objects.create(email=email, password=password, user_type=user_type, name=name)
            if user.user_type == 'employee':
                worker = Worker.objects.create(user=user)
                worker.save()
            else:
                employer = Employer.objects.create(user=user)
                employer.save()
            user.save()
            return Response({'user': UsersSerializer(user).data}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'msg': 'email field must be unique'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, **kwargs):
        try:
            user = User.objects.get(id=kwargs.get('id'))
            user.delete()
            return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)


class WorkerView(APIView):

    def get(self, request, **kwargs):
        try:
            worker = Worker.objects.get(user=kwargs.get('id'))
            exp = Experience.objects.filter(user=kwargs.get('id'))
            edu = Education.objects.filter(user=kwargs.get('id'))
            ctx = {
                'worker': WorkerSerializer(worker).data,
                'education': EduSerializer(edu).data,
                'exp': ExpSerializer(exp).data
            }
            return Response(ctx, status=status.HTTP_200_OK)
        except Worker.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, **kwargs):
        try:
            worker = Worker.objects.get(user=kwargs.get('id'))
            worker = update_worker(worker, **request.data)
            worker.save()
            return Response({'msg': 'successful updated worker'}, status=status.HTTP_200_OK)
        except Worker.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, **kwargs):
        try:
            worker = Worker.objects.get(id=kwargs.get('id'))
            worker.delete()
            return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)
        except Worker.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)