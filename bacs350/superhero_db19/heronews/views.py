from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from hero.herofunctionality import news_data
from django.urls import reverse_lazy
from os.path import exists
from .models import NewsPost

class HomeView(TemplateView):
    template_name = "home.html"
    
class NewsListView(ListView):
    template_name = "news/news.html"
    model = NewsPost

class NewsDetailView(DetailView):
    template_name = "news/news_detail.html"
    model = NewsPost
    
    def get_context_data(self, **kwargs):      
        kwargs = super().get_context_data(**kwargs)
        image = kwargs['object'].image
        image = f'static/images/{image}.jpg'
        if not exists(image):
            kwargs['missing'] = True
        kwargs["image"] = image
        return kwargs

class NewsAddView(LoginRequiredMixin, CreateView):
    template_name = "news/news_add.html"
    model = NewsPost
    fields = '__all__'
    success_url = reverse_lazy('news')
    
    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)
    
class NewsEditView(LoginRequiredMixin, UpdateView):
    template_name = "news/news_edit.html"
    success_url = reverse_lazy('news')
    model = NewsPost
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)
    
class NewsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "news/news_delete.html"
    model = NewsPost
    success_url = reverse_lazy('news')
    
    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)