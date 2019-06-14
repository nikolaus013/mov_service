from .models import Film,Projekcija,Sala

from rest_framework import viewsets,permissions,pagination
from .serializers import filmSerializer,salaSerializer,projekcijaSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = filmSerializer


class ProjekcijaViewSet(viewsets.ModelViewSet):
    queryset = Projekcija.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = projekcijaSerializer


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = salaSerializer


