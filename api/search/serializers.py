from rest_framework import serializers
from main.models import Worker, Employer, Vacancy, Cv

class CvSearchSerializer(serializers.ModelSerializer):

    owner = serializers.SerializerMethodField('get_owner')
    owner_id = serializers.SerializerMethodField('get_owner_id')
    photo_url = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = Cv
        fields = [
            'pk', 'vacancy_name', 'industry',
            'salary', 'work_type', 'pub_date',
            'owner', 'owner_id', 'photo_url',
            'grade', 'about', 'bg_header_color'
            ]

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
    
    class Meta:
        model = Vacancy
        fields = [
            'pk', 'vacancy_name', 'industry',
            'salary', 'pub_date', 'work_type',
            'owner', 'owner_id', 'photo_url',
            'address', 'leading', 'grade',
            'bg_header_color'
            ]

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
