from django.urls import path
from .views import *

urlpatterns = [
    path('create/', DepartCreate.as_view(), name = "create"),
    path('list/', DepartList.as_view(), name = 'list'),
    path("<title>/", DepartUpdateView.as_view({"get": "retrieve", "put": "update"}), name ="<title>")
]