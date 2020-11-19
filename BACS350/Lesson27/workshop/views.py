from django.views.generic import TemplateView
from markdown import markdown

from .workshop import card_data, cards_data, markdown_file_data


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

class MarkdownView(TemplateView):
    template_name='markdown.html'
    
    def get_context_data(self, **kwargs):
        md_doc = "README.md"
        return dict(markdown=markdown_data(md_doc))
    
class DocumentView(TemplateView):
    template_name = 'markdown.html'
    
    def get_context_data(self, **kwargs):
        doc = "README.md"
        card = dict(title='Doc View', body=markdown(open(doc).read()), color='bg-danger', width='col-lg-12')
        return dict(card=card)