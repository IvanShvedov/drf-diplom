from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import IntegrityError

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
            user = User.objects.create(email=email, user_type=user_type, name=name)
            user.set_password(password)
            if user.user_type == 'employee':
                worker = Worker.objects.create(user=user)
                worker.save()
            else:
                employer = Employer.objects.create(user=user)
                employer.save()
            user.save()
            return Response(UsersSerializer(user).data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'msg': 'email field must be unique'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, **kwargs):
        try:
            user = User.objects.get(id=kwargs.get('id'))
            user.delete()
            return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)


class LoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        return Response({'ok':'ok'})
        

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

    def put(self, request, **kwargs):
        try:
            employer = Employer.objects.get(user=kwargs.get('id'))
            employer = update_employer(employer, **request.data)
            employer.save()
            return Response({'msg': 'successful updated employer'}, status=status.HTTP_200_OK)
        except Employer.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)
            
    def delete(self, request, **kwargs):
        try:
            employer = Employer.objects.get(id=kwargs.get('id'))
            employer.delete()
            return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)
        except Employer.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)


class CvView(APIView):
    
    def get(self, request, **kwargs):
        try:
            cv = Cv.objects.get(id=kwargs.get('id'))
            return Response(CvSerializer(cv).data, status=status.HTTP_200_OK)
        except Cv.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            cv = Cv.objects.create()
            cv.user = User.objects.get(id=request.data.get('user_id'))
            for t in request.data.get('tags'):
                tag = Tag.objects.get_or_create(tag=t)
                if tag[1]:
                    tag[0].save()
                cv.tags.add(tag[0])
            cv = set_cv(cv, **request.data)
            cv.save()
            return Response({'cv_id': cv.id}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'msg': 'not found user'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, **kwargs):
        try:
            cv = Cv.objects.get(id=kwargs.get('id'))
            for t in request.data.get('tags'):
                tag = Tag.objects.get_or_create(tag=t)
                if tag[1]:
                    tag[0].save()
                cv.tags.add(tag[0])
            cv = set_cv(cv, **request.data)
            cv.save()
            return Response({'cv_id': cv.id}, status=status.HTTP_201_CREATED)
        except Cv.DoesNotExist:
            return Response({'msg': 'not found user'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, **kwargs):
        try:
            cv = Cv.objects.get(id=kwargs.get('id'))
            cv.delete()
            return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)
        except Cv.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)


class VacancyView(APIView):

    def get(self, request, **kwargs):
        try:
            vacancy = Vacancy.objects.get(id=kwargs.get('id'))
            return Response(VacancySerializer(vacancy).data, status=status.HTTP_200_OK)
        except Vacancy.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, **kwargs):
        try:
            vacancy = Vacancy.objects.create()
            vacancy.user = User.objects.get(id=request.data.get('user_id'))
            for t in request.data.get('tags'):
                tag = Tag.objects.get_or_create(tag=t)
                if tag[1]:
                    tag[0].save()
                vacancy.tags.add(tag[0])
            vacancy = set_vacancy(vacancy, **request.data)
            vacancy.save()
            return Response({'vacancy_id': vacancy.id}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'msg': 'not found user'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, **kwargs):
        try:
            vacancy = Vacancy.objects.get(id=kwargs.get('id'))
            for t in request.data.get('tags'):
                tag = Tag.objects.get_or_create(tag=t)
                if tag[1]:
                    tag[0].save()
                vacancy.tags.add(tag[0])
            vacancy = set_vacancy(vacancy, **request.data)
            vacancy.save()
            return Response({'cv_id': vacancy.id}, status=status.HTTP_201_CREATED)
        except Cv.DoesNotExist:
            return Response({'msg': 'not found user'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, **kwargs):
        try:
            vacancy = Vacancy.objects.get(id=kwargs.get('id'))
            vacancy.delete()
            return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)
        except Cv.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)