from django.urls import path
from .views import *


urlpatterns = [
    path('create/', UserInfoCreate.as_view(), name = "create"),
    path('<nickname>/', UserInfoUpdateView.as_view({'get': 'retrieve', 'put': 'update'}), name = 'update')
]