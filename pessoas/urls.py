from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criar', views.criar, name='criar'),
    path('editar', views.editar, name='editar')
]