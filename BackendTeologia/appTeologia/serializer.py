from rest_framework import serializers
from appTeologia.models import Estudante, Turma


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'cpf', 'telefone', 'nota', 'falta', 'status', 'turma']


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ['id', 'nome', 'dt_criacao', 'descricao', 'modulo']
