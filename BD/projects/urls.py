from django.urls import path
from .views import *


urlpatterns = [
    path('create/', projectCreate.as_view(), name="create"),
    path('list/',
         projectList.as_view(), name='list'),
    path("<title>/", projectUpdateView.as_view({"get": "retrieve", "put": "update"}), name = "<title>")
]
