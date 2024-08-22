from django.urls import path
from .views import *


urlpatterns = [
    path('create/', taskCreate.as_view(), name="create"),
    path('list/',
         taskList.as_view(), name='list'),
    path('<task>/', taskUpdateView.as_view({"get": "retrieve", "put": "update"}), name='update'),
]
