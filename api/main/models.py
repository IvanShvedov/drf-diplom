from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

from .utils import *

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
    name = models.CharField(max_length=100, blank=True, null=True, default=default_str())

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Cv(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    vacancy_name = models.CharField(max_length=100, blank=True, null=True, default=default_str())
    industry = models.CharField(max_length=200, blank=True, null=True, default=default_str())
    grade = models.CharField(max_length=200, blank=True, null=True, default=default_str())
    salary = models.IntegerField(blank=True, null=True, default=default_int())
    work_type = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())
    about = models.TextField(blank=True, null=True, default=default_str())
    bg_header_color = models.CharField(max_length=50, blank=True, null=True, default=default_str())
    pub_date = models.CharField(max_length=200, default=now(), blank=True, null=True)
    portfolio = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())

    tags = ManyToManyField('Tag')

    def __str__(self):
        return f"Vacancy: {self.vacancy_name}"


class Tag(models.Model):
    tag = models.CharField(max_length=500, blank=True, null=True, default=default_str())

    def __str__(self):
        return self.tag


class Employer(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True, default=default_str())
    mailing = models.BooleanField(blank=True, null=True, default=False)
    address = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    profile_background = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    photo_url = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    links = models.JSONField(max_length=1000, blank=True, null=True, default=default_dict())
    phone = models.JSONField(max_length=100, blank=True, null=True, default=default_dict())
    profile_link = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    about = models.TextField(blank=True, null=True, default=default_str())

    def __str__(self):
        return self.name or "null"


class Vacancy(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    vacancy_name = models.CharField(max_length=100, blank=True, null=True, default=default_str())
    industry = models.CharField(max_length=200, blank=True, null=True, default=default_str())
    salary = models.IntegerField(blank=True, null=True, default=default_int())
    work_type = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())
    experience = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    address = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    bg_header_color = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    grade = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    leading = models.CharField(max_length=200, blank=True, null=True, default=default_str())
    pub_date = models.CharField(max_length=200, default=now(), blank=True, null=True)
    trailing = models.CharField(max_length=200, blank=True, null=True, default=default_str())
    about = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())

    tags = ManyToManyField(Tag)

    def __str__(self):
        return self.vacancy_name or "null"


class Worker(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True, default=default_str())
    mailing = models.BooleanField(blank=True, null=True, default=False)
    gender = models.CharField(max_length=50, blank=True, null=True, default=default_str())
    language = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())
    birthday = models.CharField(max_length=100, blank=True, null=True, default=default_str())
    city = models.CharField(max_length=100, blank=True, null=True, default=default_str())
    phone = models.JSONField(max_length=100, blank=True, null=True, default=default_dict())
    about = models.TextField(blank=True, null=True, default=default_str())
    social_links = models.JSONField(max_length=1000, blank=True, null=True, default=default_dict())
    citizenship = models.CharField(max_length=100, blank=True, null=True, default=default_str())
    profile_link = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    photo_url = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    profile_background = models.CharField(max_length=500, blank=True, null=True, default=default_str())

    experience = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())
    education = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())

    def __str__(self):
        return self.name