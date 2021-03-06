from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('users/<int:id>', UserView.as_view(), name='users_by_id'),
    path('workers/<int:id>', WorkerView.as_view(), name='worker')
]
