from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy

from .models import Superhero


class HeroListView(ListView):
    model = Superhero
    template_name = 'hero_list.html'
    

class HeroDetailView(DetailView):
    model = Superhero
    template_name = 'hero_detail.html'
    
class HeroCreateView(CreateView):
    model = Superhero
    template_name = 'hero_new.html'
    fields = ['title', 'author', 'body']
    
class HeroUpdateView(UpdateView):
    model = Superhero
    template_name = 'hero_edit.html'
    fields = ['title', 'body']
    
class HeroDeleteView(DeleteView):
    model = Superhero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('home')

