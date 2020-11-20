from django.views.generic import TemplateView
from markdown import markdown

from .workshop import card_data, cards_data, markdown_file_data, table_data, tabs_data, accordion_data


class HomeView(TemplateView):
    template_name = 'workshop.html'


class CardView(TemplateView):
    template_name = 'card.html'
    
    def get_context_data(self, **kwargs):
        return dict(card=card_data())
    
class CardsView(TemplateView):
    template_name = 'cards.html'
    
    def get_context_data(self, **kwargs):
        return dict(cards=cards_data())
    
class DocumentView(TemplateView):
    template_name = 'markdown.html'
    
    def get_context_data(self, **kwargs):
        doc = kwargs.get('doc', "README.md")
        return markdown_file_data(doc)

class TableView(TemplateView):
    template_name = 'table.html'
    
    def get_context_data(self, **kwargs):
        return dict(table=table_data('Documents/lesson.csv'))
    
class TabsView(TemplateView):
    template_name = 'tabs.html'
    
    def get_context_data(self, **kwargs):
        tabs = tabs_data()
        return dict(title='Tab View', tabs=tabs)

class AccordionView(TemplateView):
    template_name = 'accordion.html'
    
    def get_context_data(self, **kwargs):
        return dict(accordion=accordion_data())