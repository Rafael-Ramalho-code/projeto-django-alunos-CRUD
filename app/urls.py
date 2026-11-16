from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('novo/', views.novo_alunos, name='novo_alunos'),
    path('<int:id>/', views.atualizar_alunos, name='atualizar_alunos'),
    path('<int:id>/delete/', views.deletar_alunos, name='deletar_alunos'),
]
