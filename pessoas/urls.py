from django.urls import path

from .views import IndexView,CriarView,EditarView,PessoaCreate

urlpatterns = [
   path('', IndexView.as_view(), name=''),
   path('cadastrar', PessoaCreate.as_view(), name='cadastrar')
]