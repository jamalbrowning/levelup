from django.urls import path, include
from .views import usergame_list

urlpatterns = [
    path('reports/usergames', usergame_list),
    path('', include('levelupreports.urls')),
]
