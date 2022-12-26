from django.urls import path

from .views import IndexView, PessoaCreate, PessoaUpdate


urlpatterns = [
   path('', IndexView.as_view(), name=''),
   path('cadastrar', PessoaCreate.as_view(), name='cadastrar'),
   path('editar/<int:pk>', PessoaUpdate.as_view(), name='editar')

   
]