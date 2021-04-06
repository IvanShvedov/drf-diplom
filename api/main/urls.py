from django.urls import path
from search.views import VacancySearchView, CvSearchView
from responses.views import VacancyResponseView, CvResponseView
from responses.views import VacancyWorkerResponseView, VacancyEmployerResponseView, CvWorkerResponseView, CvEmployerResponseView
from favorites.views import FavoriteView, FavoriteUserView


from .views import *

urlpatterns = [
    path('users/<int:id>', UserView.as_view(), name='users_by_id'),
    path('register/', UserView.as_view(), name='create_user'),

    path('workers/<int:id>', WorkerView.as_view(), name='worker'),
    path('employers/<int:id>', EmployerView.as_view(), name='employer'),

    path('cv/', CvView.as_view(), name='create_cv'),
    path('cv/<int:id>', CvView.as_view(), name='cv'),
    path('vacancy/', VacancyView.as_view(), name='create_vacancy'),
    path('vacancy/<int:id>', VacancyView.as_view(), name='get_vacancy'),

    path('cv/user/<int:id>', CvUserView.as_view(), name='cv_user'),
    path('vacancy/user/<int:id>', VacancyUserView.as_view(), name='vac_user'),

    path('cv/search/', CvSearchView.as_view(), name='cv_search'),
    path('vacancy/search/', VacancySearchView.as_view(), name='vacancy_search'),

    path('vacancy/response/', VacancyResponseView.as_view(), name='vacancy_response'),
    path('cv/response/', CvResponseView.as_view(), name='cv_response'),
    path('vacancy/response/<int:id>', VacancyResponseView.as_view(), name='vacancy_response_id'),
    path('cv/response/<int:id>', CvResponseView.as_view(), name='cv_response_id'),

    path('vacancy/response/worker/<int:id>', VacancyWorkerResponseView.as_view(), name='vacancy_worker_response'),
    path('vacancy/response/employer/<int:id>', VacancyEmployerResponseView.as_view(), name='vacancy_employer_response'),
    path('cv/response/worker/<int:id>', CvWorkerResponseView.as_view(), name='cv_worker_response'),
    path('cv/response/employer/<int:id>', CvEmployerResponseView.as_view(), name='cv_employer_response'),

#GET favorites/vacancy/ favorites/cv/
    path('favorites/vacancy/', FavoriteUserView.as_view(), name='favorite_user_vacancy'),
    path('favorites/cv/', FavoriteUserView.as_view(), name='favorite_user_cv'),
    # path('favorites/user/<int:id>', FavoriteView.as_view(), name='favorite_user'),
    path('favorites/', FavoriteView.as_view(), name='favorite'),
    path('favorites/<int:id>', FavoriteView.as_view(), name='favorite'),
]
