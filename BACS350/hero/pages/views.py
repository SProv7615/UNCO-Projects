from django.views.generic import TemplateView

class HeroView(TemplateView):
    template_name='hero.html'

class VillainView(TemplateView):
    template_name='villain.html'

# Create your views here.
