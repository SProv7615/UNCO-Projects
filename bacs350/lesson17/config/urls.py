from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

class HeroView(TemplateView):
    template_name = "hero.html"
    
    def get_context_data(self, **kwargs):
        return {
            'title': "Heroes Destroying The World?",
            'body': "No, they really aren't. We just wanted to see if you'd give us money for that ridiculous title.",
        }
class HeroDisplay(TemplateView):
    template_name = "hero_display.html"
    
    def get_context_data(self, **kwargs):
        return {
            'title': "Superhero Exposed!",
            'name': "Iron Man",
            'identity': "Tony Stark",   
        }

urlpatterns = [
    path('', HeroView.as_view(template_name="hero.html")),
    path('display/', HeroDisplay.as_view(template_name="hero_display.html")),
    path('admin/', admin.site.urls),
]
