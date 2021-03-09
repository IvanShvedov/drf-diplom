import json
from re import split
from django.db.models import query
from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import CharField, ListField
from .models import *


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'user_type']


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = '__all__'

class EmployerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['tag']

class CvSerializer(serializers.ModelSerializer):

    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cv
        fields = '__all__'

class VacancySerializer(serializers.ModelSerializer):

    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Vacancy
        fields = '__all__'

    
    