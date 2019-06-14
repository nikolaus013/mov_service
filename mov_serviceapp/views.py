from rest_framework import generics
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Sala, Projekcija, Film
from rest_framework.settings import api_settings
from .serializers import filmSerializer, salaSerializer, projekcijaSerializer

from rest_framework.response import Response


class FilmList(generics.ListCreateAPIView):
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS

    # The style to use for queryset pagination.
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    queryset = Film.objects.all()
    serializer_class = filmSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def filter_queryset(self, queryset):

        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request):
        serializer = filmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete(self, request, pk):
    film = get_object_or_404(Film, pk=pk)
    film.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = filmSerializer
