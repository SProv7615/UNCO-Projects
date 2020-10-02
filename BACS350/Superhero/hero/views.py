from django.views.generic import TemplateView
from django.http import HttpResponse
    
class SpidermanView(TemplateView):
    template_name = 'spiderman.html'
    
class BatmanView(TemplateView):
    template_name = 'batman.html'
    
class IronManView(TemplateView):
    template_name = 'ironman.html'
    
class DeadpoolView(TemplateView):
    template_name = 'deadpool.html'
    
class WolverineView(TemplateView):
    template_name = 'wolverine.html'
