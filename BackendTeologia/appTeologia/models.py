from django.db import models


class Turma(models.Model):
    nome = models.CharField(max_length=30, default='')
    dt_criacao = models.CharField(max_length=10, default='')
    descricao = models.CharField(max_length=150, default='')
    modulo = models.CharField(max_length=4, default='')

    def __str__(self):
        return '%s %s %s %s' % (self.nome, self.dt_criacao, self.descricao, self.modulo)


class Estudante(models.Model):
    nome = models.CharField(max_length=30, default='')
    cpf = models.CharField(max_length=11, default='')
    telefone = models.CharField(max_length=11, default='')
    nota = models.CharField(max_length=4, default='')
    falta = models.CharField(max_length=3, default='')
    status = models.CharField(max_length=1, default='')
    turma = models.ForeignKey(
        Turma, verbose_name="the related poll", on_delete=models.CASCADE,)

    def __str__(self):
        return self.nome
