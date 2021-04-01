from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.request import HttpRequest
from rest_framework import status


from main.models import VacancyResponse, CvResponse
from .serializers import VacancyResponseSerializer, CvResponseSerializer

class VacancyResponseView(APIView):

    def get(self, request: HttpRequest, **kwargs):
        try:
            vacancy_response = VacancyResponse.objects.get(id=kwargs.get('id'))
            return Response(VacancyResponseSerializer(vacancy_response).data, status=status.HTTP_200_OK)   
        except VacancyResponse.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request: HttpRequest):
        serializer = VacancyResponseSerializer(data=request.data)
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
        serializer = CvResponseSerializer(data=request.data)
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