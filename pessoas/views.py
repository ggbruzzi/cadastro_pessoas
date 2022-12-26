from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Pessoa
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'index.html'

class CriarView(TemplateView):
    template_name = 'index2.html'

class EditarView(TemplateView):
    template_name = 'index3.html'

class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome_pessoa','sobrenome','idade','data_nascimento','email','apelido','observação']
    template_name = 'form.html'
    success_url = reverse_lazy('')


