from django.urls import path
from .views import *


urlpatterns = [
    path('create/', RankCreate.as_view(), name = "create"),
    path('list/', RankList.as_view(), name = 'list'),
    path('<role>/', RankUpdateView.as_view({"get": "retrieve", "put": "update"}), name ='<role>')
]