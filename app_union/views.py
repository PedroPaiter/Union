from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import TipoUsuario, Usuario
import logging


def home(request):
  return render(request, 'home.html')

def cadastrar_usuario(request):
  if request.method == 'POST':
    usuario = Usuario()
    usuario.nome = request.POST.get('nome')
    usuario.sobrenome = request.POST.get('sobrenome')
    usuario.email = request.POST.get('email')
    usuario.recebe_notificacao = request.POST.get('recebe_notificacao') != None  # Convert to boolean
    usuario.tipo_usuario = request.POST.get('tipo_usuario')
    usuario.ra = request.POST.get('ra')
    usuario.uc = request.POST.get('uc')
    usuario.nome_projeto = request.POST.get('nome_projeto')
    usuario.tema_trabalho = request.POST.get('tema_trabalho')
    usuario.instituicao_matriz = request.POST.get('instituicao_matriz')
    usuario.save()

    return HttpResponseRedirect('cadastro_concluido')
  else:
    context = {
      'tipos_usuarios': TipoUsuario.choices
    }
    return render(request, 'usuarios/cadastro_usuarios.html', context)
  
def cadastro_concluido(request):
  context = {
    'count_usuarios': Usuario.objects.count()
  }

  return render(request, 'usuarios/cadastro_concluido.html', context)

def relatorio_usuarios(request):
  usuarios = Usuario.objects.all()

  context = {
    'aluno': usuarios.filter(tipo_usuario=TipoUsuario.ALUNO).count(),
    'aluno_expositor': usuarios.filter(tipo_usuario=TipoUsuario.ALUNO_EXPOSITOR).count(),
    'professor': usuarios.filter(tipo_usuario=TipoUsuario.PROFESSOR).count(),
    'professor_outra_iess': usuarios.filter(tipo_usuario=TipoUsuario.PROFESSOR_OUTRA_IESS).count(),
    'avaliador': usuarios.filter(tipo_usuario=TipoUsuario.AVALIADOR).count(),
    'visitante': usuarios.filter(tipo_usuario=TipoUsuario.VISITANTE).count(),
  }

  return render(request, 'usuarios/relatorio_usuarios.html', {'dados_grafico': context, 'usuarios': usuarios})