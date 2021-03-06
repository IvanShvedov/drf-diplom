from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import *
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
            if user.user_type == 'employee':
                worker = Worker.objects.create(user=user)
                worker.save()
            else:
                employer = Employer.objects.create(user=user)
                employer.save()
            user.save()
            return Response({'user': UsersSerializer(user).data}, status=200)
        except IntegrityError:
            return Response({'msg': 'email field must be unique'}, status=400)

    def delete(self, request, **kwargs):
        try:
            user = User.objects.get(id=kwargs.get('id'))
            user.delete()
            return Response({'msg': 'deleted'}, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'not found'}, status=404)


class WorkerView(APIView):

    def get(self, request, **kwargs):
        try:
            worker = Worker.objects.get(user=kwargs.get('id'))
            return Response(WorkerSerializer(worker).data, status=200)
        except Worker.DoesNotExist:
            return Response({'msg': 'not found'}, status=404)

    def put(self, request, **kwargs):
        try:
            worker = Worker.objects.get(user=kwargs.get('id'))
            worker = update_worker(worker, **request.data)
            worker.save()
            return Response({'msg': 'successful updated worker'}, status=200)
        except Worker.DoesNotExist:
            return Response({'msg': 'not found'}, status=404)

    def delete(self, request, **kwargs):
        try:
            worker = Worker.objects.get(id=kwargs.get('id'))
            worker.delete()
            return Response({'msg': 'deleted'}, status=200)
        except Worker.DoesNotExist:
            return Response({'msg': 'not found'}, status=404)