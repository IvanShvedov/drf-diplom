from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.request import HttpRequest
from rest_framework import status
from rest_framework.settings import api_settings
import jwt


from main.paginator import MyPaginationMixin
from main.models import Favorite, User
from .serializers import FavoriteSerializer, FavoriteCvSerializer, FavoriteVacancySerializer
from main.utils import get_payload


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
            payload = get_payload(request)
            fav = Favorite.objects.get(user__id=payload['user_id'], item_id=kwargs.get('id'))
            fav.delete()
            return Response({"msg": "ok"}, status=status.HTTP_200_OK)
        except Favorite.DoesNotExist:
            return Response({"msg": "not found"}, status=status.HTTP_404_NOT_FOUND)
        except jwt.DecodeError:
            return Response({"msg": "decode error"}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.ExpiredSignatureError:
            return Response({"msg": "expired error"}, status=status.HTTP_403_FORBIDDEN)


class FavoriteUserView(APIView, MyPaginationMixin):

    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request: HttpRequest, **kwargs):
        ctx = {}
        try:
            payload = get_payload(request)
            if payload is not None:
                ctx = {
                    'user_id': payload['user_id'],
                }
            if 'cv' in request.get_full_path():
                qset = Favorite.objects.filter(user=payload['user_id'], item_type='cv')
            else:
                qset = Favorite.objects.filter(user=payload['user_id'], item_type='vacancy')

            page = self.paginate_queryset(qset)
            if page is not None:
                if 'cv' in request.get_full_path():
                    return self.get_paginated_response(FavoriteCvSerializer(page, many=True, context=ctx).data)
                else:
                    return self.get_paginated_response(FavoriteVacancySerializer(page, many=True, context=ctx).data)
            else:
                return Response({"msg": "page not found"}, status=status.HTTP_404_NOT_FOUND)
        except jwt.DecodeError:
            return Response({"msg": "decode error"}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.ExpiredSignatureError:
            return Response({"msg": "expired error"}, status=status.HTTP_403_FORBIDDEN)
        except TypeError:
            return Response({"msg": "type error"}, status=status.HTTP_401_UNAUTHORIZED)
