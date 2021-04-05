from rest_framework import fields, serializers
from main.models import VacancyResponse, CvResponse, Cv, Vacancy, Worker, Employer


class VacancyResponseSerializer(serializers.ModelSerializer):

    vacancy = serializers.SerializerMethodField('get_vacancy')
    employer_avatar = serializers.SerializerMethodField('get_emp_avatar')
    worker_avatar = serializers.SerializerMethodField('get_wrk_avatar')
    worker_name = serializers.SerializerMethodField('get_wrk_name')
    employer_name = serializers.SerializerMethodField('get_emp_name')

    class Meta:
        model = VacancyResponse
        fields = ['vacancy_response', 'worker', 'employer', 'worker_cv', 'message',
                'state', 'date_response', 'vacancy',
                'employer_avatar', 'worker_avatar', 'worker_name', 'employer_name'
        ]

    def get_wrk_name(self, obj):
        try:
            worker = Worker.objects.get(id=obj.worker.id)
            return worker.name
        except Worker.DoesNotExist:
            return ''

    def get_emp_name(self, obj):
        try:
            employer = Employer.objects.get(id=obj.employer.id)
            return employer.name
        except Employer.DoesNotExist:
            return ''

    def get_vacancy(self, obj):
        try:
            vac = Vacancy.objects.get(pk=obj.vacancy_response.id)
            return vac.vacancy_name
        except Vacancy.DoesNotExist:
            return ''

    def get_wrk_avatar(self, obj):
        try:
            worker = Worker.objects.get(id=obj.worker.id)
            return worker.photo_url
        except Worker.DoesNotExist:
            return ''

    def get_emp_avatar(self, obj):
        try:
            employer = Employer.objects.get(id=obj.employer.id)
            return employer.photo_url
        except Employer.DoesNotExist:
            return ''

class CvResponseSerializer(serializers.ModelSerializer):

    cv = serializers.SerializerMethodField('get_cv')
    employer_avatar = serializers.SerializerMethodField('get_emp_avatar')
    worker_avatar = serializers.SerializerMethodField('get_wrk_avatar')
    worker_name = serializers.SerializerMethodField('get_wrk_name')
    employer_name = serializers.SerializerMethodField('get_emp_name')

    class Meta:
        model = CvResponse
        fields = ['cv_response', 'employer', 'worker',
                'vacancy', 'message', 'state', 'date_response', 'cv',
                'employer_avatar', 'worker_avatar', 'worker_name', 'employer_name'
            ]

    def get_wrk_name(self, obj):
        try:
            worker = Worker.objects.get(id=obj.worker.id)
            return worker.name
        except Worker.DoesNotExist:
            return ''

    def get_emp_name(self, obj):
        try:
            employer = Employer.objects.get(id=obj.employer.id)
            return employer.name
        except Employer.DoesNotExist:
            return ''

    def get_cv(self, obj):
        try:
            cv = Cv.objects.get(pk=obj.cv_response.id)
            return cv.vacancy_name
        except Cv.DoesNotExist:
            return ''

    def get_wrk_avatar(self, obj):
        try:
            worker = Worker.objects.get(id=obj.worker.id)
            return worker.photo_url
        except Worker.DoesNotExist:
            return ''

    def get_emp_avatar(self, obj):
        try:
            employer = Employer.objects.get(id=obj.employer.id)
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