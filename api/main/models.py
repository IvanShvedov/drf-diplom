from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

import json


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    user_type = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class About(models.Model):
    vacancy = models.ForeignKey('Vacancy', models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    points = models.CharField(max_length=500, blank=True, null=True)


class Cv(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    vacancy_name = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    grade = models.CharField(max_length=200, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    work_type = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    bg_header_color = models.CharField(max_length=50, blank=True, null=True)
    pub_date = models.CharField(max_length=100, blank=True, null=True)


class CvTag(models.Model):
    cvs = ManyToManyField(Cv)
    tag = models.CharField(max_length=500, blank=True, null=True)


class Education(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    profession = models.CharField(max_length=200, blank=True, null=True)
    university = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=500, blank=True, null=True)
    start_year = models.CharField(max_length=500, blank=True, null=True)
    end_year = models.CharField(max_length=500, blank=True, null=True)


class Employer(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    mailing = models.BooleanField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    profile_background = models.CharField(max_length=500, blank=True, null=True)
    photo_url = models.CharField(max_length=500, blank=True, null=True)
    links = models.CharField(max_length=1000, blank=True, null=True)
    phone = models.CharField(max_length=33, blank=True, null=True)
    profile_link = models.CharField(max_length=500, blank=True, null=True)
    about = models.TextField(blank=True, null=True)


class Experience(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    start_year = models.CharField(max_length=500, blank=True, null=True)
    end_year = models.CharField(max_length=500, blank=True, null=True)


class Portfolio(models.Model):
    cv = models.ForeignKey(Cv, models.CASCADE, blank=True, null=True)
    img_link = models.CharField(max_length=500, blank=True, null=True)
    source_link = models.CharField(max_length=500, blank=True, null=True)


class Vacancy(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    vacancy_name = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    work_type = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    bg_header_color = models.CharField(max_length=500, blank=True, null=True)
    grade = models.CharField(max_length=500, blank=True, null=True)
    leading = models.CharField(max_length=200, blank=True, null=True)
    pub_date = models.CharField(max_length=100, blank=True, null=True)
    trailing = models.CharField(max_length=200, blank=True, null=True)


class VacancyTag(models.Model):
    vacancies = ManyToManyField(Vacancy)
    tag = models.CharField(max_length=500, blank=True, null=True)


class Worker(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    mailing = models.BooleanField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    language = models.JSONField(max_length=500, blank=True, null=True)
    birthday = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    phone = models.JSONField(max_length=100, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    social_links = models.JSONField(max_length=1000, blank=True, null=True)
    citizenship = models.CharField(max_length=100, blank=True, null=True)
    profile_link = models.CharField(max_length=500, blank=True, null=True)
    photo_url = models.CharField(max_length=500, blank=True, null=True)
    profile_background = models.CharField(max_length=500, blank=True, null=True)
