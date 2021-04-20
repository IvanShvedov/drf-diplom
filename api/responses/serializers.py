from rest_framework import fields, serializers
from main.models import VacancyResponse, CvResponse, Cv, Vacancy, Worker, Employer


class VacancyResponseSerializer(serializers.ModelSerializer):

    vacancy_name = serializers.SerializerMethodField('get_vacancy')
    employer_avatar = serializers.SerializerMethodField('get_emp_avatar')
    worker_avatar = serializers.SerializerMethodField('get_wrk_avatar')
    employer_name = serializers.SerializerMethodField('get_emp_name')
    worker_name = serializers.SerializerMethodField('get_wrk_name')
    cv_name = serializers.SerializerMethodField('get_cv')

    class Meta:
        model = VacancyResponse
        fields = ['id', 'vacancy', 'worker', 'employer', 'cv', 'message',
                'state', 'date_response', 'vacancy_name',
                'employer_avatar', 'worker_avatar', 'worker_name', 'employer_name', 'cv_name'
        ]

    def get_cv(self, obj):
        try:
            return obj.cv.vacancy_name
        except Cv.DoesNotExist:
            return ''

    def get_wrk_name(self, obj):
        try:
            worker = Worker.objects.get(user=obj.worker.id)
            return worker.name
        except Worker.DoesNotExist:
            return ''

    def get_emp_name(self, obj):
        try:
            employer = Employer.objects.get(user=obj.employer.id)
            return employer.name
        except Employer.DoesNotExist:
            return ''

    def get_vacancy(self, obj):
        try:
            return obj.vacancy.vacancy_name
        except Vacancy.DoesNotExist:
            return ''

    def get_wrk_avatar(self, obj):
        try:
            worker = Worker.objects.get(user=obj.worker.id)
            return worker.photo_url
        except Worker.DoesNotExist:
            return ''

    def get_emp_avatar(self, obj):
        try:
            employer = Employer.objects.get(user=obj.employer.id)
            return employer.photo_url
        except Employer.DoesNotExist:
            return ''

class CvResponseSerializer(serializers.ModelSerializer):

    cv_name = serializers.SerializerMethodField('get_cv')
    employer_avatar = serializers.SerializerMethodField('get_emp_avatar')
    worker_avatar = serializers.SerializerMethodField('get_wrk_avatar')
    worker_name = serializers.SerializerMethodField('get_wrk_name')
    employer_name = serializers.SerializerMethodField('get_emp_name')
    vacancy_name = serializers.SerializerMethodField('get_vacancy')

    class Meta:
        model = CvResponse
        fields = ['id', 'cv', 'employer', 'worker', 'vacancy',
                'vacancy_name', 'message', 'state', 'date_response', 'cv_name',
                'employer_avatar', 'worker_avatar', 'worker_name', 'employer_name'
            ]

    def get_vacancy(self, obj):
        try:
            return obj.vacancy.vacancy_name
        except Vacancy.DoesNotExist:
            return ''

    def get_wrk_name(self, obj):
        try:
            worker = Worker.objects.get(user=obj.worker.id)
            return worker.name
        except Worker.DoesNotExist:
            return ''

    def get_emp_name(self, obj):
        try:
            employer = Employer.objects.get(user=obj.employer.id)
            return employer.name
        except Employer.DoesNotExist:
            return ''

    def get_cv(self, obj):
        try:
            return obj.cv.vacancy_name
        except Cv.DoesNotExist:
            return ''

    def get_wrk_avatar(self, obj):
        try:
            worker = Worker.objects.get(user=obj.worker.id)
            return worker.photo_url
        except Worker.DoesNotExist:
            return ''

    def get_emp_avatar(self, obj):
        try:
            employer = Employer.objects.get(user=obj.employer.id)
            return employer.photo_url
        except Employer.DoesNotExist:
            return ''


class InVacancyResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacancyResponse
        fields = '__all__'


class InCvResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CvResponse
        fields = '__all__'