from rest_framework import viewsets
from appTeologia.models import Estudante, Turma
from appTeologia.serializer import EstudanteSerializer, TurmaSerializer


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer


class TurmasViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
