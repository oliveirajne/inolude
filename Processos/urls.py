from django.urls import path
from .models import Processo
from .views import list_processos

urlpatterns = [
    path('', list_processos, name='list_processos'),
]