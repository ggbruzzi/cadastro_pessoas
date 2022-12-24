from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class CriarView(TemplateView):
    template_name = 'index2.html'

class EditarView(TemplateView):
    template_name = 'index3.html'


