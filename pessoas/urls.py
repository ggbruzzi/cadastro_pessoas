from django.urls import path

from .views import IndexView,CriarView,EditarView,PessoaCreate

urlpatterns = [
   path('', IndexView.as_view(), name=''),
   path('criar', CriarView.as_view(), name='criar'),
   path('editar', EditarView.as_view(), name='editar'),
   path('cadastrar/pessoa', PessoaCreate.as_view(), name='cadastrar-pessoa')
]