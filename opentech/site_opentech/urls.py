from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('servicos/', ServicosView.as_view(), name='servicos'),
    path('clientes/', ClientesView.as_view(), name='clientes'),
    path('parceiros/', ParceirosView.as_view(), name='parceiros'),
    path('beneficios_contratacao/', ContratacaoView.as_view(), name='beneficios_contratacao'),
    path('info_institucionais/', InfoInstitucionaisView.as_view(), name='info_institucionais'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('contato/', ContatoView.as_view(), name='contato'),
]