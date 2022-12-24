from django.urls import path

from .views import IndexView,CriarView,EditarView

urlpatterns = [
   path('', IndexView.as_view(), name=''),
   path('criar', CriarView.as_view(), name='criar'),
   path('editar', EditarView.as_view(), name='editar')
]