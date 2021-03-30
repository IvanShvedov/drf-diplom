from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.request import HttpRequest
from rest_framework.settings import api_settings

from .filters import Filter
from main.models import Tag, Cv, Vacancy
from .serializers import *
from main.paginator import MyPaginationMixin


class CvSearchView(APIView, MyPaginationMixin):
    
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 

    def get(self, request: HttpRequest):
        try:
            cv = Cv.objects.all()
            if request.GET:
                cv = Filter(cv).filt(request)
            page = self.paginate_queryset(cv)
            if page is not None:
                return self.get_paginated_response(VacancySearchSerializer(page, many=True).data)
            else:
                return Response({"msg": "page not found"}, status=status.HTTP_404_NOT_FOUND)
        except Tag.DoesNotExist:
            return Response({"msg": "tag not found"}, status=status.HTTP_404_NOT_FOUND)
        except Tag.MultipleObjectsReturned:
            return Response({"msg": "tag is none"}, status=status.HTTP_404_NOT_FOUND)


class VacancySearchView(APIView, MyPaginationMixin):
    
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 

    def get(self, request: HttpRequest):
        try:
            vacancy = Vacancy.objects.all()
            if request.GET:
                vacancy = Filter(vacancy).filt(request)
            page = self.paginate_queryset(vacancy)
            if page is not None:
                return self.get_paginated_response(VacancySearchSerializer(page, many=True).data)
            else:
                return Response({"msg": "page not found"}, status=status.HTTP_404_NOT_FOUND)
        except Tag.DoesNotExist:
            return Response({"msg": "tag not found"}, status=status.HTTP_404_NOT_FOUND)
        except Tag.MultipleObjectsReturned:
            return Response({"msg": "tag is none"}, status=status.HTTP_404_NOT_FOUND)
