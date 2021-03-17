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


class CvSearchSerializer(serializers.ModelSerializer):

    owner = serializers.SerializerMethodField('get_owner')
    owner_id = serializers.SerializerMethodField('get_owner_id')
    photo_url = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = Cv
        fields = ['pk', 'vacancy_name', 'industry', 'salary', 'work_type', 'pub_date', 'owner', 'owner_id', 'photo_url']

    def get_owner(self, obj):
        try:
            owner = Worker.objects.get(user=obj.user)
        except Worker.DoesNotExist:
            return ''
        return owner.name
    
    def get_owner_id(self, obj):
        try:
            owner = Worker.objects.get(user=obj.user)
        except Worker.DoesNotExist:
            return ''
        return owner.pk

    def get_photo_url(self, obj):
        try:
            owner = Worker.objects.get(user=obj.user)
        except Worker.DoesNotExist:
            return ''
        return owner.photo_url


class VacancySearchSerializer(serializers.ModelSerializer):
    
    owner = serializers.SerializerMethodField('get_owner')
    owner_id = serializers.SerializerMethodField('get_owner_id')
    photo_url = serializers.SerializerMethodField('get_photo_url')
    
    class Meta:
        model = Vacancy
        fields = ['pk', 'vacancy_name', 'industry', 'salary', 'pub_date', 'work_type', 'owner', 'owner_id', 'photo_url']

    def get_owner(self, obj):
        try:
            owner = Employer.objects.get(user=obj.user)
        except Employer.DoesNotExist:
            return ''
        return owner.name

    def get_owner_id(self, obj):
        try:
            owner = Employer.objects.get(user=obj.user)
        except Employer.DoesNotExist:
            return ''
        return owner.pk

    def get_photo_url(self, obj):
        try:
            owner = Employer.objects.get(user=obj.user)
        except Employer.DoesNotExist:
            return ''
        return owner.photo_url