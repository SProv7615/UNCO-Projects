from django.urls import path, include

from .views import CardView, CardsView, DocumentView, HomeView, TableView, TabsView, AccordionView


urlpatterns = [
    
    path('', HomeView.as_view(), name='workshop'),
    path('card', CardView.as_view(), name='card'),
    path('cards', CardsView.as_view(), name='cards'),
    path('doc/<str:doc>', DocumentView.as_view(), name='doc'),
    path('table', TableView.as_view(), name='table'),
    path('tabs', TabsView.as_view(), name='tabs'),
    path('accordion', AccordionView.as_view(), name='accordion')
    
    
]
