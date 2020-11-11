from django.urls import path, include

from .views import AboutView, HomeView, CardView, CardsView


urlpatterns = [
    
    path('', HomeView.as_view(), name='workshop'),
    path('about', AboutView.as_view(), name='base'),
    path('card', CardView.as_view(), name='card'),
    path('cards', CardsView.as_view(), name='cards'),
    
    
]
