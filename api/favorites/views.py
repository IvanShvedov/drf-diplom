from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.request import HttpRequest
from rest_framework import status
from rest_framework.settings import api_settings


from main.paginator import MyPaginationMixin
from main.models import Favorite, User
from .serializers import FavoriteSerializer


class FavoriteView(APIView, MyPaginationMixin):

    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request: HttpRequest, **kwargs):
        try:
            fav_set = Favorite.objects.filter(user=kwargs.get('id'))
            page = self.paginate_queryset(fav_set)
            if page is not None:
                return self.get_paginated_response(FavoriteSerializer(page, many=True).data)
            else:
                return Response({"msg": "page not found"}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"msg": "user not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request: HttpRequest):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"id": serializer.data['id']}, status=status.HTTP_201_CREATED)

    def delete(self, request: HttpRequest, **kwargs):
        try:
            fav = Favorite.objects.get(id=kwargs.get('id'))
            fav.delete()
            return Response({"msg": "ok"}, status=status.HTTP_200_OK)
        except Favorite.DoesNotExist:
            return Response({"msg": "not found"}, status=status.HTTP_404_NOT_FOUND)