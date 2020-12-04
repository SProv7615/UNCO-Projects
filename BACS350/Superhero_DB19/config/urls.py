from hero.views import HeroAddView, HeroDeleteView, HeroDetailView, HeroEditView, HeroListView, HeroDocumentView
from heronews.views import NewsListView
from django.urls import path, include

urlpatterns = [
    path('', include('heronews.urls')),
    path('', include('accounts.urls')),
    path('gallery', HeroListView.as_view(), name='hero_list'),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('add', HeroAddView.as_view(), name='hero_add'),
    path('edit/<int:pk>/', HeroEditView.as_view(), name='hero_edit'),
    path('delete/<int:pk>/', HeroDeleteView.as_view(), name='hero_delete'), 
    path('<str:doc>', HeroDocumentView.as_view(), name='doc'),
]
