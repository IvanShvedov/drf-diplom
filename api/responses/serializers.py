from rest_framework import serializers
from main.models import VacancyResponse, CvResponse


class VacancyResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacancyResponse
        fields = '__all__'

class CvResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CvResponse
        fields = '__all__'
