from rest_framework import routers
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mov_serviceapp import views
from .api import FilmViewSet, SalaViewSet, ProjekcijaViewSet

router = routers.DefaultRouter()
router.register('api/mov_serviceapp', FilmViewSet, 'movies')

urlpatterns = [

    path('mov_serviceapp/', views.FilmList.as_view()),
    path('mov_serviceapp/<int:pk>/', views.FilmList.as_view()),

]
