from datetime import datetime, timedelta

from django.db.models.manager import BaseManager
from . import models
from django.contrib.postgres.search import SearchVector


class Filter:

    model = None

    def __init__(self, model):
        self.model = model
        self.filters = {
            'phrase': self._phrase_filter,
            'tag': self._tags_filter,
            'vacancy-name': self._vacancy_name_filter,
            'industry': self._industry_filter,
            'max-salary': self._max_salary_filter,
            'min-salary': self._min_salary_filter,
            'grades': self._grades_filter,
            'work-type': self._work_type_filter,
            'experience': self._experience_filter,
            'pub-date': self._pub_date_filter,
        }

    def filt(self, request):
        for query in request.GET:
            self.filters[query](request.GET.getlist(query))
        return self.model

    def _phrase_filter(self, phrase):
        if phrase[0]:
            if isinstance(self.model, (models.Vacancy.objects,)):
                self.model = self.model.annotate(search=SearchVector(
                    'vacancy_name', 'industry',
                    'leading', 'trailing', 'body'
                    )).filter(search=phrase[0])
            else:
                self.model = self.model.annotate(search=SearchVector(
                    'vacancy_name', 'industry', 'about'
                    )).filter(search=phrase[0])                

    def _tags_filter(self, tags):
        for tag in tags:
            tag = models.Tag.objects.get(tag__iexact=tag)
            self.model = self.model.filter(tags=tag)

    def _vacancy_name_filter(self, vacancy_name):
        if vacancy_name[0]:
            self.model = self.model.filter(vacancy_name__icontains=vacancy_name[0])

    def _industry_filter(self, industry):
        if industry[0]:
            self.model = self.model.filter(industry__icontains=industry[0])
    
    def _max_salary_filter(self, max_salary):
        if max_salary[0]:
            self.model = self.model.filter(salary__lte=int(max_salary[0]))

    def _min_salary_filter(self, min_salary):
        if min_salary[0]:
            self.model = self.model.filter(salary__gte=int(min_salary[0]))
    
    def _grades_filter(self, grades):
        for grade in grades:
            self.model = self.model.filter(grade__iexact=grade)
    
    def _work_type_filter(self, work_type):
        for work in work_type:
            self.model = self.model.filter(work_type__icontains=work)
    
    def _experience_filter(self, experience):
        for exp in experience:
            self.model = self.model.filter(experience__icontains=exp)
    
    def _pub_date_filter(self, pub_date):
        if pub_date[0]:
            self.model = self.filter_by_pub_date(pub_date[0])

    def _filter_by_pub_date(self, pub_date):
        if pub_date == 'day':
            today = datetime.today()
            search_day = today - timedelta(days=1)
            self.model = self.model.filter(pub_date__gte=search_day)
        elif pub_date == 'three-days':
            today = datetime.today()
            search_day = today - timedelta(days=3)
            self.model = self.model.filter(pub_date__gte=search_day)
        elif pub_date == 'week':
            today = datetime.today()
            search_day = today - timedelta(days=7)
            self.model = self.model.filter(pub_date__gte=search_day)
        elif pub_date == 'two-weeks':
            today = datetime.today()
            search_day = today - timedelta(days=14)
            self.model = self.model.filter(pub_date__gte=search_day)
        elif pub_date == 'month':
            today = datetime.today()
            search_day = today - timedelta(days=30)
            self.model = self.model.filter(pub_date__gte=search_day)

