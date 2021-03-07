from django.urls import path
from .views import *

urlpatterns = [
    path('users/<int:id>', UserView.as_view(), name='users_by_id'),
    path('users/', UserView.as_view(), name='create_user'),
    path('workers/<int:id>', WorkerView.as_view(), name='worker'),
    path('employers/<int:id>', EmployerView.as_view(), name='employer'),
    path('cv/', CvView.as_view(), name='create_cv'),
    path('cv/<int:id>', CvView.as_view(), name='get_cv')
]
