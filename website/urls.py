from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('funcionarios/', views.listar_funcionarios, name='listar'),
    path('funcionario/<int:id>/', views.detalhes_funcionario, name='detalhes'),
    path('cadastrar/', views.cadastrar_funcionario, name='cadastrar'),
    path('editar/<int:id>/', views.editar_funcionario, name='editar'),
    path('excluir/<int:id>/', views.excluir_funcionario, name='excluir'),
]