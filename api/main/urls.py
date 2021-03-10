from django.urls import path
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
    path('cv/search', CvSearchView.as_view(), name='cv_search')
]
