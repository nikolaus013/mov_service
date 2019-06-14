from rest_framework import routers
from django.urls import path
from django.urls import path, re_path, include

from rest_framework.urlpatterns import format_suffix_patterns
from mov_serviceapp import views
from .api import FilmViewSet, SalaViewSet, ProjekcijaViewSet

router = routers.DefaultRouter()
router.register('api/mov_serviceapp', FilmViewSet, 'movies')

urlpatterns = [

    path('mov_serviceapp/', views.FilmList.as_view()),
    path('mov_serviceapp/<int:pk>/$', views.FilmList.as_view()),
    path(r'^mov_serviceapp/api/?P<pk>[0-9]+)/$', views.FilmDetail.as_view())
    #re_path('api/(?P<version>(v1|v2))/', include('mov_serviceapp.urls'))

]
