from rest_framework import serializers
from .models import User, Worker, Employer, Vacancy, Cv, Tag, CvResponse, VacancyResponse, Favorite


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
    got_responsed = serializers.SerializerMethodField('get_response')
    favorite = serializers.SerializerMethodField('get_favorite')

    class Meta:
        model = Cv
        fields = '__all__'

    def get_response(self, obj):
        try:
            user_id = self.context.get('user_id')
            CvResponse.objects.get(employer=user_id, cv=obj.id)
            return True
        except CvResponse.DoesNotExist:
            return False

    def get_favorite(self, obj):
        try:
            user_id = self.context.get('user_id')
            Favorite.objects.get(user=user_id, item_id=obj.id)
            return True
        except Favorite.DoesNotExist:
            return False


class VacancySerializer(serializers.ModelSerializer):

    tags = serializers.StringRelatedField(many=True)
    got_responsed = serializers.SerializerMethodField('get_response')
    favorite = serializers.SerializerMethodField('get_favorite')

    class Meta:
        model = Vacancy
        fields = '__all__'

    def get_response(self, obj):
        try:
            user_id = self.context.get('user_id')
            VacancyResponse.objects.get(worker=user_id, vacancy=obj.id)
            return True
        except VacancyResponse.DoesNotExist:
            return False

    def get_favorite(self, obj):
        try:
            user_id = self.context.get('user_id')
            Favorite.objects.get(user=user_id, item_id=obj.id)
            return True
        except Favorite.DoesNotExist:
            return False