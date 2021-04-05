from rest_framework import serializers
from main.models import Worker, Employer, Vacancy, Cv, CvResponse, VacancyResponse


class CvSearchSerializer(serializers.ModelSerializer):

    owner = serializers.SerializerMethodField('get_owner')
    owner_id = serializers.SerializerMethodField('get_owner_id')
    photo_url = serializers.SerializerMethodField('get_photo_url')
    got_responsed = serializers.SerializerMethodField('get_response')

    class Meta:
        model = Cv
        fields = [
            'pk', 'vacancy_name', 'industry',
            'salary', 'work_type', 'pub_date',
            'owner', 'owner_id', 'photo_url',
            'grade', 'about', 'bg_header_color',
            'got_responsed'
            ]

    def get_response(self, obj):
        try:
            user_id = self.context.get('user_id')
            CvResponse.objects.get(employer=user_id, cv=obj.id)
            return True
        except CvResponse.DoesNotExist:
            return False

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
        return owner.user.pk

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
    got_responsed = serializers.SerializerMethodField('get_response')
    
    class Meta:
        model = Vacancy
        fields = [
            'pk', 'vacancy_name', 'industry',
            'salary', 'pub_date', 'work_type',
            'owner', 'owner_id', 'photo_url',
            'address', 'leading', 'grade',
            'bg_header_color', 'got_responsed'
            ]

    def get_response(self, obj):
        try:
            user_id = self.context.get('user_id')
            VacancyResponse.objects.get(worker=user_id, vacancy=obj.id)
            return True
        except VacancyResponse.DoesNotExist:
            return False

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
        return owner.user.pk

    def get_photo_url(self, obj):
        try:
            owner = Employer.objects.get(user=obj.user)
        except Employer.DoesNotExist:
            return ''
        return owner.photo_url
