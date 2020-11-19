from django.urls import path, include

from .views import CardView, CardsView, DocumentView, HomeView


urlpatterns = [
    
    path('', HomeView.as_view(), name='workshop'),
    path('card', CardView.as_view(), name='card'),
    path('cards', CardsView.as_view(), name='cards'),
    path('doc', DocumentView.as_view(), name='doc'),
    
    
]
