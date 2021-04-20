from typing import Type
from django.core.mail import send_mail

from main.models import VacancyResponse, CvResponse


class ResponseNotifyService:

    def __init__(self, serializer, response_to: str):
        try:
            if 'vacancy' in response_to:
                response = VacancyResponse.objects.filter(vacancy=serializer['vacancy'], worker=serializer['worker']).first()
                response_name = response.vacancy.vacancy_name
                self.subject = 'На вашу вакансию "{0}" откликнулись'.format(response_name)
                self.to_email = response.employer.email
            else:
                response = CvResponse.objects.filter(cv=serializer['cv'], employer=serializer['employer']).first()
                response_name = response.cv.vacancy_name
                self.subject = 'На ваше резюме "{0}" откликнулись'.format(response_name)
                self.to_email = response.worker.email
            self.message = serializer['message']
            self.from_email = 'helperrsender@gmail.com'
        except CvResponse.DoesNotExist:
            pass
        except VacancyResponse.DoesNotExist:
            pass


    def send(self):
        send_mail(
            subject=self.subject,
            message=self.message,
            from_email=self.from_email,
            recipient_list=[self.to_email],
            fail_silently=True
        )

