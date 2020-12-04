from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # new
from django.urls import reverse_lazy

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    fields = '__all__'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_add.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)
    
class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = '__all__'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(UserPassesTestMixin, DeleteView): # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user