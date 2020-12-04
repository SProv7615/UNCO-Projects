from django.views.generic import TemplateView
from markdown import markdown

from .workshop import accordion_data, card_data, cards_data, carousel_data, markdown_file_data, table_data, tabs_data 
from .menu import load_menu, load_side_menu

class HomeView(TemplateView):
    template_name = 'workshop.html'

class AccordionView(TemplateView):
    template_name = 'super.html'
    
    def get_context_data(self, **kwargs):
        return dict(accordion=accordion_data())
        
class CardView(TemplateView):
    template_name = 'super.html'
    
    def get_context_data(self, **kwargs):
        return dict(card=card_data(), menu = load_menu('README.md'))
    
class CardsView(TemplateView):
    template_name = 'super.html'
    
    def get_context_data(self, **kwargs):
        return dict(cards=cards_data(), menu = load_menu('README.md'))
    
class CarouselView(TemplateView):
    template_name = 'super.html'
    
    def get_context_data(self, **kwargs):
        carousel = carousel_data()
        return dict(title='Carousel View', carousel=carousel, menu = load_menu('README.md'))    
    
class DocumentView(TemplateView):
    template_name = 'markdown.html'
    
    def get_context_data(self, **kwargs):
        menu = load_menu('README.md')
        doc = kwargs.get('doc', "README.md")
        return dict(card=markdown_file_data(doc), menu = load_menu('README.md'))

class TableView(TemplateView):
    template_name = 'super.html'
    
    def get_context_data(self, **kwargs):
        return dict(title='Lesson Schedules', table=table_data('Documents/lesson.csv'), menu = load_menu('README.md'))
    
class TabsView(TemplateView):
    template_name = 'super.html'
    
    def get_context_data(self, **kwargs):
        tabs = tabs_data()
        return dict(title='Tab View', tabs=tabs, menu = load_menu('README.md'))

class SuperView(TemplateView):
    template_name = 'super.html'
    
    def get_context_data(self, **kwargs):
        return super_data()