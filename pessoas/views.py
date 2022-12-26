from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,UpdateView
from .models import Pessoa
from django.urls import reverse_lazy

class IndexView(ListView):
    model = Pessoa
    template_name = 'index.html'


class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome_pessoa','sobrenome','idade','data_nascimento','email','apelido','observação']
    template_name = 'form.html'
    success_url = reverse_lazy('')

class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_pessoa','sobrenome','idade','data_nascimento','email','apelido','observação']
    template_name = 'form.html'
    success_url = reverse_lazy('')


