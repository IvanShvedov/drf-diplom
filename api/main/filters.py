from datetime import datetime, timedelta
from . import models
from django.contrib.postgres.search import SearchVector


def filter_vacancy(vacancy, request):

    phrase = request.GET.get('phrase')
    tags = request.GET.getlist('tag')
    vacancy_name = request.GET.get('vacancy-name')
    industry = request.GET.get('industry')
    max_salary = request.GET.get('max-salary')
    min_salary = request.GET.get('min-salary')
    grades = request.GET.getlist('grade')
    work_type = request.GET.getlist('work-type')
    experience = request.GET.getlist('experience')
    pub_date = request.GET.get('pub-date')

    if phrase:
        vacancy = models.Vacancy.objects.annotate(search=SearchVector('vacancy_name', 'industry', 'leading', 'trailing', 'body')).filter(search=phrase)
    for tag in tags:
        tag = models.Tag.objects.get(tag__iexact=tag)
        vacancy = vacancy.filter(tags=tag)
    if vacancy_name:
        vacancy = vacancy.filter(vacancy_name__icontains=vacancy_name)
    if industry:
        vacancy = vacancy.filter(industry__icontains=industry)
    if max_salary:
        vacancy = vacancy.filter(salary__lte=max_salary)
    if min_salary:
        vacancy = vacancy.filter(salary__gte=min_salary)
    for grade in grades:
        vacancy = vacancy.filter(grade__iexact=grade)
    for work in work_type:
        vacancy = vacancy.filter(work_type__icontains=work)
    for exp in experience:
        vacancy = vacancy.filter(experience__icontains=exp)
    if pub_date:
        vacancy = filter_by_pub_date(vacancy, pub_date)

    return vacancy


def filter_cv(cv, request):

    phrase = request.GET.get('phrase')
    tags = request.GET.getlist('tag')
    vacancy_name = request.GET.get('vacancy-name')
    industry = request.GET.get('industry')
    max_salary = request.GET.get('max-salary')
    min_salary = request.GET.get('min-salary')
    grades = request.GET.getlist('grade')
    work_type = request.GET.getlist('work-type')
    pub_date = request.GET.get('pub-date')

    if phrase:
        cv = models.Cv.objects.annotate(search=SearchVector('vacancy_name', 'industry', 'about')).filter(search=phrase)
    for tag in tags:
        tag = models.Tag.objects.get(tag__iexact=tag)
        cv = cv.filter(tags=tag)
    if vacancy_name:
        cv = cv.filter(vacancy_name__icontains=vacancy_name)
    if industry:
        cv = cv.filter(industry__icontains=industry)
    if max_salary:
        cv = cv.filter(salary__lte=max_salary)
    if min_salary:
        cv = cv.filter(salary__gte=min_salary)
    for grade in grades:
        cv = cv.filter(grade__iexact=grade)
    for work in work_type:
        cv = cv.filter(work_type__icontains=work)
    if pub_date:
        cv = filter_by_pub_date(cv, pub_date)

    return cv


def filter_by_pub_date(model, pub_date):
    if pub_date == 'day':
        today = datetime.today()
        search_day = today - timedelta(days=1)
        model = model.filter(pub_date__gte=search_day)
    elif pub_date == 'three-days':
        today = datetime.today()
        search_day = today - timedelta(days=3)
        model = model.filter(pub_date__gte=search_day)
    elif pub_date == 'week':
        today = datetime.today()
        search_day = today - timedelta(days=7)
        model = model.filter(pub_date__gte=search_day)
    elif pub_date == 'two-weeks':
        today = datetime.today()
        search_day = today - timedelta(days=14)
        model = model.filter(pub_date__gte=search_day)
    elif pub_date == 'month':
        today = datetime.today()
        search_day = today - timedelta(days=30)
        model = model.filter(pub_date__gte=search_day)
    return model