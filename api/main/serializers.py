import json
from re import split
from django.db.models import query
from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import CharField, ListField
from .models import *


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'email', 'user_type', 'name']


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

class CvSearchSerializer(serializers.ModelSerializer):

    owner = serializers.SerializerMethodField('get_owner')

    class Meta:
        model = Cv
        fields = ['pk', 'vacancy_name', 'industry', 'salary', 'work_type', 'pub_date', 'owner']

    def get_owner(self, obj):
        try:
            owner = Worker.objects.get(user=obj.user)
        except Worker.DoesNotExist:
            return ''
        return owner.name

class VacancySearchSerializer(serializers.ModelSerializer):
    
    owner = serializers.SerializerMethodField('get_owner')
    
    class Meta:
        model = Vacancy
        fields = ['pk', 'vacancy_name', 'industry', 'salary', 'pub_date', 'work_type', 'owner']

    def get_owner(self, obj):
        try:
            owner = Employer.objects.get(user=obj.user)
        except Employer.DoesNotExist:
            return ''
        return owner.name