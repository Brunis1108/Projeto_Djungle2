from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.listar_funcionarios, name='index'),
    path('funcionario/<int:id>/', views.detalhes_funcionario, name='detalhes'),
    path('editar/<int:id>/', views.editar_funcionario, name='editar'),
    path('excluir/<int:id>/', views.excluir_funcionario, name='excluir'),

]