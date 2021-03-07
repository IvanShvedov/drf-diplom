from django.urls import path
from .views import *

urlpatterns = [
    path('users/<int:id>', UserView.as_view(), name='users_by_id'),
    path('users/', UserView.as_view(), name='create_user'),
    path('workers/<int:id>', WorkerView.as_view(), name='worker')
]
