from django.db import models

class TipoUsuario(models.IntegerChoices):
  ALUNO = 1, "Aluno"
  ALUNO_EXPOSITOR = 2, "Aluno Expositor"
  PROFESSOR = 3, "Professor"
  PROFESSOR_OUTRA_IESS = 4, "Professor de outra IESS"
  AVALIADOR = 5, "Avaliador"
  VISITANTE = 6, "Visitante"

class Usuario(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.TextField(max_length=30)
  sobrenome = models.TextField(max_length=30)
  email = models.TextField(max_length=70)
  recebe_notificacao = models.BooleanField()
  tipo_usuario = models.IntegerField(
    max_length=1,
    choices=TipoUsuario.choices,
    default=TipoUsuario.ALUNO,
  )
  ra = models.TextField(max_length=10, null=True, blank=True)
  uc = models.TextField(max_length=10, null=True, blank=True)
  nome_projeto = models.TextField(max_length=100, null=True, blank=True)
  tema_trabalho = models.TextField(max_length=100, null=True, blank=True)
  instituicao_matriz = models.TextField(max_length=100, null=True, blank=True)