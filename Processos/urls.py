from django.urls import path
from .views import list_processos, create_processo, update_processo, delete_processo

app_name = 'Processos'

urlpatterns = [
    path('', list_processos, name='list_processos'),
    path('new', create_processo, name='create_processo'),
    path('update/<int:id>/', update_processo, name='update_processo'),
    path('delete/<int:id>/', delete_processo, name='delete_processo'),
]