from django.urls import path
from app_union import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/cadastro', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/cadastro_concluido', views.cadastro_concluido, name='cadastro_concluido'),
    path('usuarios/relatorio_usuarios', views.relatorio_usuarios, name='relatorio_usuarios')
]
