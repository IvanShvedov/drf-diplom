from rest_framework import serializers
from .models import User, Worker, Employer, Vacancy, Cv, Tag


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

