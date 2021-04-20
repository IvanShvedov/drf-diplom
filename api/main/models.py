from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

from .utils import default_str, default_dict, now, default_address

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

    def __str__(self):
        return f"ID: {self.pk}, EMAIL: {self.email}"


class Cv(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    vacancy_name = models.CharField(max_length=100, blank=True, null=True, default=default_str())
    industry = models.CharField(max_length=200, blank=True, null=True, default=default_str())
    grade = models.CharField(max_length=200, blank=True, null=True, default=default_str())
    salary = models.IntegerField(blank=True, null=True, default=-1)
    work_type = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())
    about = models.TextField(blank=True, null=True, default=default_str())
    bg_header_color = models.CharField(max_length=50, blank=True, null=True, default=default_str())
    pub_date = models.DateTimeField(default=now(), blank=True, null=True)
    portfolio = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())

    tags = ManyToManyField('Tag', blank=True, null=True)

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
    address = models.JSONField(max_length=500, blank=True, null=True, default=default_address())
    profile_background = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    photo_url = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    links = models.JSONField(max_length=1000, blank=True, null=True, default=default_dict())
    phone = models.JSONField(max_length=100, blank=True, null=True, default=default_dict())
    profile_link = models.CharField(max_length=500, blank=True, null=True, default="empty")
    about = models.TextField(blank=True, null=True, default=default_str())

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class Vacancy(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    vacancy_name = models.CharField(max_length=100, blank=True, null=True, default=default_str())
    industry = models.CharField(max_length=200, blank=True, null=True, default=default_str())
    salary = models.IntegerField(blank=True, null=True, default=-1)
    work_type = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())
    experience = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    address = models.JSONField(max_length=700, blank=True, null=True, default=default_address())
    bg_header_color = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    grade = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    leading = models.CharField(max_length=400, blank=True, null=True, default=default_str())
    pub_date = models.DateTimeField(default=now(), blank=True, null=True)
    trailing = models.CharField(max_length=400, blank=True, null=True, default=default_str())
    body = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())

    tags = ManyToManyField(Tag, blank=True, null=True)

    def __str__(self):
        return f"ID: {self.id}, Vacancy: {self.vacancy_name}"


class Worker(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True, default=default_str())
    mailing = models.BooleanField(blank=True, null=True, default=False)
    gender = models.CharField(max_length=50, blank=True, null=True, default=default_str())
    language = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())
    birthday = models.CharField(max_length=100, blank=True, null=True, default=default_str())
    address = models.JSONField(max_length=500, blank=True, null=True, default=default_address())
    phone = models.JSONField(max_length=100, blank=True, null=True, default=default_dict())
    about = models.TextField(blank=True, null=True, default=default_str())
    social_links = models.JSONField(max_length=1000, blank=True, null=True, default=default_dict())
    citizenship = models.CharField(max_length=100, blank=True, null=True, default=default_str())
    profile_link = models.CharField(max_length=500, blank=True, null=True, default="empty")
    photo_url = models.CharField(max_length=500, blank=True, null=True, default=default_str())
    profile_background = models.CharField(max_length=500, blank=True, null=True, default=default_str())

    experience = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())
    education = models.JSONField(max_length=500, blank=True, null=True, default=default_dict())

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class VacancyResponse(models.Model):
    vacancy = models.ForeignKey(Vacancy, models.CASCADE)
    worker = models.ForeignKey(User, models.CASCADE, related_name='vacancy_worker')
    employer = models.ForeignKey(User, models.CASCADE, related_name='vacancy_employer')
    cv = models.ForeignKey(Cv, models.CASCADE)
    message = models.TextField(blank=True, null=True, default=default_str())
    state = models.CharField(max_length=100, blank=True, null=True, default="sent")
    date_response = models.DateTimeField(default=now(), blank=True, null=True)

    def __str__(self):
        return f"ID: {self.id}, Worker: {self.worker}, Employer: {self.employer}"


class CvResponse(models.Model):
    cv = models.ForeignKey(Cv, models.CASCADE)
    employer = models.ForeignKey(User, models.CASCADE, related_name='cv_employer')
    worker = models.ForeignKey(User, models.CASCADE, related_name='cv_worker')
    vacancy = models.ForeignKey(Vacancy, models.CASCADE)
    message = models.TextField(blank=True, null=True, default=default_str())
    state = models.CharField(max_length=100, blank=True, null=True, default="sent")
    date_response = models.DateTimeField(default=now(), blank=True, null=True)

    def __str__(self):
        return f"ID: {self.id}, Employer: {self.employer}, Worker: {self.worker}"


class Favorite(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True, default=-1)
    item_type = models.CharField(max_length=100, blank=True, null=True, default="vacancy")

    def __str__(self):
        return f"ID: {self.id}, User: {self.user}"

