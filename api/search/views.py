from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.request import HttpRequest
from rest_framework.settings import api_settings
import jwt

from .filters import Filter
from main.models import Tag, Cv, Vacancy
from .serializers import *
from main.paginator import MyPaginationMixin
from main.utils import get_payload


class CvSearchView(APIView, MyPaginationMixin):
    
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 

    def get(self, request: HttpRequest):
        cv = Cv.objects.all().order_by('-pub_date')
        context={}
        statuscode = status.HTTP_200_OK
        try:
            try:
                payload = get_payload(request)
            except jwt.DecodeError:
                pass
            except jwt.ExpiredSignatureError:
                statuscode = status.HTTP_401_UNAUTHORIZED
            if request.GET:
                cv = Filter(cv).filt(request)
            if payload is not None:
                context={'user_id': payload.get('user_id')}
            page = self.paginate_queryset(cv)
            if page is not None:
                return self.get_paginated_response(CvSearchSerializer(page, many=True, context=context).data, status=statuscode)
            else:
                return Response({"msg": "page not found"}, status=status.HTTP_404_NOT_FOUND)
        except Tag.DoesNotExist:
            return Response({"msg": "tag not found"}, status=status.HTTP_404_NOT_FOUND)
        except Tag.MultipleObjectsReturned:
            return Response({"msg": "tag is none"}, status=status.HTTP_404_NOT_FOUND)


class VacancySearchView(APIView, MyPaginationMixin):
    
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 

    def get(self, request: HttpRequest):
        vacancy = Vacancy.objects.all().order_by('-pub_date')
        context={}
        statuscode = status.HTTP_200_OK
        try:
            try:
                payload = get_payload(request)
            except jwt.DecodeError:
                pass
            except jwt.ExpiredSignatureError:
                statuscode = status.HTTP_401_UNAUTHORIZED
            if request.GET:
                vacancy = Filter(vacancy).filt(request)
            if payload is not None:
                context={'user_id': payload.get('user_id')}
            page = self.paginate_queryset(vacancy)
            if page is not None:
                return self.get_paginated_response(VacancySearchSerializer(page, many=True, context=context).data, status=statuscode)
            else:
                return Response({"msg": "page not found"}, status=status.HTTP_404_NOT_FOUND)
        except Tag.DoesNotExist:
            return Response({"msg": "tag not found"}, status=status.HTTP_404_NOT_FOUND)
        except Tag.MultipleObjectsReturned:
            return Response({"msg": "tag is none"}, status=status.HTTP_404_NOT_FOUND)
