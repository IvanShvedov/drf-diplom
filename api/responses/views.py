from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.request import HttpRequest
from rest_framework import status
from rest_framework.settings import api_settings

from main.models import VacancyResponse, CvResponse
from main.paginator import MyPaginationMixin
from .serializers import VacancyResponseSerializer, CvResponseSerializer, InCvResponseSerializer, InVacancyResponseSerializer


class VacancyResponseView(APIView):

    def get(self, request: HttpRequest, **kwargs):
        try:
            vacancy_response = VacancyResponse.objects.get(id=kwargs.get('id'))
            return Response(VacancyResponseSerializer(vacancy_response).data, status=status.HTTP_200_OK)   
        except VacancyResponse.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request: HttpRequest):
        context = {'init': 'worker'}
        serializer = InVacancyResponseSerializer(data=request.data, context=context)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"id": serializer.data['id']}, status=status.HTTP_201_CREATED)

    def put(self, request: HttpRequest):
        try:
            vac_id = request.data.get('id')
            state = request.data.get('state')
            vac = VacancyResponse.objects.get(id=vac_id)
            vac.state = state
            vac.save()
            return Response({"msg": "ok"}, status=status.HTTP_200_OK)
        except VacancyResponse.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request: HttpRequest, **kwargs):
        try:
            vac_id = kwargs.get('id')
            vac = VacancyResponse.objects.get(id=vac_id)
            vac.delete()
            return Response({"msg": "ok"}, status=status.HTTP_200_OK)
        except VacancyResponse.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)


class CvResponseView(APIView):

    def get(self, request, **kwargs):
        try:
            vacancy_response = CvResponse.objects.get(id=kwargs.get('id'))
            return Response(CvResponseSerializer(vacancy_response).data, status=status.HTTP_200_OK)   
        except CvResponse.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request: HttpRequest):
        context = {'init': 'employer'}
        serializer = InCvResponseSerializer(data=request.data, context=context)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"id": serializer.data['id']}, status=status.HTTP_201_CREATED)

    def put(self, request: HttpRequest):
        try:
            vac_id = request.data.get('id')
            state = request.data.get('state')
            vac = CvResponse.objects.get(id=vac_id)
            vac.state = state
            vac.save()
            return Response({"msg": "ok"}, status=status.HTTP_200_OK)
        except CvResponse.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: HttpRequest, **kwargs):
        try:
            vac_id = kwargs.get('id')
            vac = CvResponse.objects.get(id=vac_id)
            vac.delete()
            return Response({"msg": "ok"}, status=status.HTTP_200_OK)
        except CvResponse.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)


class VacancyWorkerResponseView(APIView, MyPaginationMixin):

    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request, **kwagrs):
        vacancy_responses = VacancyResponse.objects.filter(worker__id = kwagrs.get('id'))
        page = self.paginate_queryset(vacancy_responses)
        if page is not None:
            return self.get_paginated_response(VacancyResponseSerializer(page, many=True).data)
        else:
            return Response({"msg": "page not found"}, status=status.HTTP_404_NOT_FOUND)


class VacancyEmployerResponseView(APIView, MyPaginationMixin):

    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 

    def get(self, request, **kwargs):
        vacancy_responses = VacancyResponse.objects.filter(employer__id = kwargs.get('id'))
        page = self.paginate_queryset(vacancy_responses)
        if page is not None:
            return self.get_paginated_response(VacancyResponseSerializer(page, many=True).data)
        else:
            return Response({"msg": "page not found"}, status=status.HTTP_404_NOT_FOUND)


class CvWorkerResponseView(APIView, MyPaginationMixin):

    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 

    def get(self, request, **kwargs):
        vacancy_responses = CvResponse.objects.filter(worker__id = kwargs.get('id'))
        page = self.paginate_queryset(vacancy_responses)
        if page is not None:
            return self.get_paginated_response(CvResponseSerializer(page, many=True).data)
        else:
            return Response({"msg": "page not found"}, status=status.HTTP_404_NOT_FOUND)


class CvEmployerResponseView(APIView, MyPaginationMixin):

    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 

    def get(self, request, **kwargs):
        vacancy_responses = CvResponse.objects.filter(employer__id = kwargs.get('id'))
        page = self.paginate_queryset(vacancy_responses)
        if page is not None:
            return self.get_paginated_response(CvResponseSerializer(page, many=True).data)
        else:
            return Response({"msg": "page not found"}, status=status.HTTP_404_NOT_FOUND)
