from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from os.path import exists
from .models import Superhero
from .herofunctionality import card_data, markdown_file_data

#class HeroView(TemplateView):
#    template_name = "hero_detail.html"
#    
#   def get_context_data(self, **kwargs):
#        hero = Superhero.objects.get(pk=1)
#        return {'hero': hero, 'css': '/static/hero.css'}

class HeroDetailView(DetailView):
    template_name = "hero_detail.html"
    model = Superhero
    
    def get_context_data(self, **kwargs):      
        kwargs = super().get_context_data(**kwargs)
        image = kwargs['object'].image
        image = f'static/images/{image}.jpg'
        if not exists(image):
            kwargs['missing'] = True
        kwargs["image"] = image
        return kwargs
    
class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Superhero


class HeroAddView(LoginRequiredMixin, CreateView):
    template_name = "hero_add.html"
    model = Superhero
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)
    
class HeroEditView(LoginRequiredMixin, UpdateView):
    template_name = "hero_edit.html"
    model = Superhero
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)

#    Code to get 'if something were edit view vs add view', this can detect.
#    def get_context_data(self, **kwargs):      
#        kwargs = super(heroEditView,
#                      self).get_context_data(**kwargs)
#        kwargs['edit'] = True
#        return Kwargs
    
class HeroDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "hero_delete.html"
    model = Superhero
    success_url = reverse_lazy('hero_list')
    
    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)
    
class HeroDocumentView(TemplateView):
    template_name = 'markdown.html'
    
    def get_context_data(self, **kwargs):
        doc = kwargs.get('doc', "about.md")
        return dict(card=markdown_file_data(doc))