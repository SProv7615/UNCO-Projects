from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Superhero

#class HeroView(TemplateView):
#    template_name = "hero_detail.html"
#    
#   def get_context_data(self, **kwargs):
#        hero = Superhero.objects.get(pk=1)
#        return {'hero': hero, 'css': '/static/hero.css'}

class HeroDetailView(DetailView):
    template_name = "hero_detail.html"
    model = Superhero
    
class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Superhero

class HeroAddView(CreateView):
    template_name = "hero_add.html"
    model = Superhero
    fields = '__all__'
    
class HeroEditView(UpdateView):
    template_name = "hero_edit.html"
    model = Superhero
    fields = '__all__'

#    Code to get 'if something were edit view vs add view', this can detect.
#    def get_context_data(self, **kwargs):      
#        kwargs = super(heroEditView,
#                      self).get_context_data(**kwargs)
#        kwargs['edit'] = True
#        return Kwargs
    
class HeroDeleteView(DeleteView):
    template_name = "hero_delete.html"
    model = Superhero
    success_url = reverse_lazy('hero_list')