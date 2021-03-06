from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']