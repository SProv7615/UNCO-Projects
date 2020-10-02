from django.views.generic import TemplateView
from django.http import HttpResponse


class PageView(TemplateView):
    template_name = 'home.html'
    
class AboutView(TemplateView):
    template_name = 'about.html'

