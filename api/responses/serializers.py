from rest_framework import serializers
from main.models import VacancyResponse, CvResponse, Cv, Vacancy, Worker, Employer


class VacancyResponseSerializer(serializers.ModelSerializer):

    vacancy = serializers.SerializerMethodField('get_vacancy')
    employer_avatar = serializers.SerializerMethodField('get_emp_avatar')
    worker_avatar = serializers.SerializerMethodField('get_wrk_avatar')

    class Meta:
        model = VacancyResponse
        fields = ['vacancy_response', 'worker', 'employer', 'worker_cv', 'message'
                'state', 'date_response', 'vacancy',
                'employer_avatar', 'worker_avatar'
        ]

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
            employer = Employer.objects.get(id=obj.worker.id)
            return employer.photo_url
        except Employer.DoesNotExist:
            return ''

class CvResponseSerializer(serializers.ModelSerializer):

    cv = serializers.SerializerMethodField('get_cv')
    employer_avatar = serializers.SerializerMethodField('get_emp_avatar')
    worker_avatar = serializers.SerializerMethodField('get_wrk_avatar')
    
    class Meta:
        model = CvResponse
        fields = ['cv_response', 'employer', 'worker',
                'vacancy', 'message', 'state', 'date_response', 'cv',
                'employer_avatar', 'worker_avatar'
            ]

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
            employer = Employer.objects.get(id=obj.worker.id)
            return employer.photo_url
        except Employer.DoesNotExist:
            return ''