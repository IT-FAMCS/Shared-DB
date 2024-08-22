'''from django.urls import path
from .views import *


urlpatterns = [
    path('create/', vacationsCreate.as_view(), name="create"),
    path('<short_title>/',
         vacationsCreate.as_view({'get': 'retrieve', 'put': 'update'}), name='update')
]
'''