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
            return Response(WorkerSerializer(worker).data, status=status.HTTP_200_OK)
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


class EmployerView(APIView):

    def get(self, request, **kwargs):
        try:
            employer = Employer.objects.get(user=kwargs.get('id'))
            return Response(EmployerSerializer(employer).data, status=status.HTTP_200_OK)
        except Employer.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, **kwargs):
        try:
            employer = Employer.objects.get(user=kwargs.get('id'))
            employer = update_employer(employer, **request.data)
            employer.save()
            return Response({'msg': 'successful updated employer'}, status=status.HTTP_200_OK)
        except Worker.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)
            
    def delete(self, request, **kwargs):
        try:
            employer = Employer.objects.get(id=kwargs.get('id'))
            employer.delete()
            return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)
        except Worker.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)


class CvView(APIView):
    
    def get(self, request, **kwargs):
        pass

    def post(self, request):
        pass