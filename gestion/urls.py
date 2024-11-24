# gestion/urls.py
from django.urls import path
from .views import ProgramasListView, ProgramaCreateView, ProgramaUpdateView, ProgramaDeleteView

urlpatterns = [
    path('', ProgramasListView.as_view(), name='programas_list'),
    path('nuevo/', ProgramaCreateView.as_view(), name='programa_create'),
    path('editar/<int:pk>/', ProgramaUpdateView.as_view(), name='programa_edit'),
    path('eliminar/<int:pk>/', ProgramaDeleteView.as_view(), name='programa_delete'),
]
