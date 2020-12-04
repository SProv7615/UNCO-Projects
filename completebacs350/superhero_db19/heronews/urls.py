from django.urls import path, include
from .views import HomeView, NewsListView, NewsDetailView, NewsAddView, NewsEditView, NewsDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('newsreel', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news/add', NewsAddView.as_view(), name='news_add'),
    path('news/edit/<int:pk>/', NewsEditView.as_view(), name='news_edit'),
    path('news/delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'), 
]

