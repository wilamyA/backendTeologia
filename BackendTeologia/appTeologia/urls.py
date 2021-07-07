from django.urls import path, include
from . import views
from appTeologia.views import EstudanteViewSet, TurmasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'estudantes', EstudanteViewSet)
router.register(r'turmas', TurmasViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
