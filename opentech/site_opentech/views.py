from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'site/index.html'

class PortfolioView(TemplateView):
    template_name = 'site/portfolio.html'

class ServicosView(TemplateView):
    template_name = 'site/servicos.html'

class ClientesView(TemplateView):
    template_name = 'site/clientes.html'

class ParceirosView(TemplateView):
    template_name = 'site/parceiros.html'

class ContratacaoView(TemplateView):
    template_name = 'site/beneficios_contratacao.html'

class InfoInstitucionaisView(TemplateView):
    template_name = 'site/info_institucionais.html'

class SobreView(TemplateView):
    template_name = 'site/sobre.html'

class ContatoView(TemplateView):
    template_name = 'site/contato.html'