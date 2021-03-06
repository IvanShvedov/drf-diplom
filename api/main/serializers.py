from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
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