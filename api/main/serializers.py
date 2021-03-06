from rest_framework import serializers
from .models import *


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'user_type']