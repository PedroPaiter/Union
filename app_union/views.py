from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from .models import TipoUsuario, Usuario
from django.urls import reverse

def home(request):
  return render(request, 'home.html')

def cadastrar_usuario(request, id=None):
    # Se tem ID, é edição. Se não, é cadastro novo
    usuario = get_object_or_404(Usuario, pk=id) if id else None
    
    if request.method == 'POST':
        # Se for edição, pega o usuário existente, senão cria novo
        if not usuario:
            usuario = Usuario()
        
        # Preenche os dados do formulário
        usuario.nome = request.POST.get('nome')
        usuario.sobrenome = request.POST.get('sobrenome')
        usuario.email = request.POST.get('email')
        usuario.recebe_notificacao = request.POST.get('recebe_notificacao') is not None
        usuario.tipo_usuario = request.POST.get('tipo_usuario')
        usuario.ra = request.POST.get('ra')
        usuario.uc = request.POST.get('uc')
        usuario.nome_projeto = request.POST.get('nome_projeto')
        usuario.tema_trabalho = request.POST.get('tema_trabalho')
        usuario.instituicao_matriz = request.POST.get('instituicao_matriz')
        usuario.save()

        return HttpResponseRedirect(reverse('cadastro_concluido'))
    
    # Contexto para o template
    context = {
        'usuario': usuario,
        'tipos_usuarios': TipoUsuario.choices,
        'modo_edicao': id is not None  # Indica se está no modo edição
    }
    return render(request, 'usuarios/cadastro_usuarios.html', context)

def deletar_registro(request, id):
    registro = get_object_or_404(Usuario, pk=id)
    
    if request.method == 'POST':
        registro.delete()
        return redirect('relatorio_usuarios')


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