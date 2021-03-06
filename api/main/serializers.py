import json
from re import split
from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import CharField, ListField
from .models import *


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'user_type']

class ExpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = '__all__'

class EduSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Education
        fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = '__all__'

class EmployerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'