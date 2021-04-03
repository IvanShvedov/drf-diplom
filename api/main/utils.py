from datetime import datetime
from django.contrib.postgres.search import SearchVector
from django.http.request import HttpRequest


def update_worker(model, **kwargs):
    model.name = kwargs.get('name')
    model.mailing = kwargs.get('mailing')
    model.gender = kwargs.get('gender')
    model.language = kwargs.get('language')
    model.birthday = kwargs.get('birthday')
    model.address = kwargs.get('address')
    model.phone = kwargs.get('phone')
    model.about = kwargs.get('about')
    model.social_links = kwargs.get('social_links')
    model.citizenship = kwargs.get('citizenship')
    model.profile_link = kwargs.get('profile_link')
    model.photo_url = kwargs.get('photo_url')
    model.profile_background = kwargs.get('profile_background')

    model.experience = kwargs.get('experience')
    model.education = kwargs.get('education')
    return model


def update_employer(model, **kwargs):
    model.name = kwargs.get('name')
    model.mailing = kwargs.get('mailing')
    model.address = kwargs.get('address')
    model.profile_background = kwargs.get('profile_background')
    model.photo_url = kwargs.get('photo_url')
    model.links = kwargs.get('links')
    model.phone = kwargs.get('phone')
    model.profile_link = kwargs.get('profile_link')
    model.about = kwargs.get('about')
    return model


def set_cv(model, **kwargs):
    model.vacancy_name = kwargs.get('vacancy_name')
    model.industry = kwargs.get('industry')
    model.grade = kwargs.get('grade')
    model.salary = kwargs.get('salary')
    model.work_type = kwargs.get('work_type')
    model.about = kwargs.get('about')
    model.bg_header_color = kwargs.get('bg_header_color')
    model.portfolio = kwargs.get('portfolio')
    return model

def set_vacancy(model, **kwargs):
    model.vacancy_name = kwargs.get('vacancy_name')
    model.industry = kwargs.get('industry')
    model.salary = kwargs.get('salary')
    model.work_type = kwargs.get('work_type')
    model.experience = kwargs.get('experience')
    model.address = kwargs.get('address')
    model.grade = kwargs.get('grade')
    model.leading = kwargs.get('leading')
    model.bg_header_color = kwargs.get('bg_header_color')
    model.trailing = kwargs.get('trailing')
    model.body = kwargs.get('body')
    return model


def default_str():
    return ""

def default_dict():
    return list

def default_int():
    return 0

def now():
    return datetime.now()

def default_address():
    return None


import jwt
from api import settings
def get_payload(request: HttpRequest):
    token = request.headers.get('authorization')
    if token is None:
        return None
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    return payload