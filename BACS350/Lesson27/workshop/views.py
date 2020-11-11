from django.views.generic import TemplateView

text = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repudiandae amet consequuntur iure inventore animi. Nihil sunt, aut. Autem obcaecati aliquam nulla rem, quam rerum, ab quidem, doloribus natus dolores voluptatem.'''

class HomeView(TemplateView):
    template_name = 'workshop.html'

class BaseView(TemplateView):
    template_name = 'theme.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class CardView(TemplateView):
    template_name = 'card.html'
    
    def get_context_data(self, **kwargs):
        data = dict(title="Cards are Great", body=text)
        return dict(card=data, title="Card View Layout")
    
class CardsView(TemplateView):
    template_name = 'cards.html'
    
    def get_context_data(self, **kwargs):
        return dict(cards=cards_data())

def lorem(num_chars):
    text = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium quibusdam sit hic, ipsum labore commodi eligendi quos culpa maxime voluptate. Ad, voluptatem, esse! Quam accusantium minus sequi cumque minima quod odio accusamus assumenda dolorem consequuntur esse alias nisi, explicabo error! Dolores blanditiis adipisci laboriosam quo sequi nostrum consectetur recusandae illo sed molestias laborum, ullam modi doloremque. Facilis nulla iure odit accusamus. Doloremque voluptatibus repudiandae, beatae temporibus odit suscipit eius facere dolores quibusdam perspiciatis exercitationem velit porro cupiditate repellendus et tempora dolorem, sapiente, debitis cum nihil sunt. Illo perspiciatis cumque qui quia quam quibusdam doloribus fugiat porro, soluta esse nesciunt itaque? Blanditiis, voluptate, voluptates iure iste aut maxime perferendis aliquid, odit doloribus sapiente temporibus ad mollitia consequuntur, alias totam tenetur ut. Accusantium voluptas temporibus, ea a impedit.'''
    return text[:num_chars]
    
def cards_data():
    return [
        dict(title="Card 1", body=lorem(200), color='bg-success'),
        dict(title="Card 2", body=lorem(150), color='bg-info'),
        dict(title="Card 3", body=lorem(20), color='bg-primary'),
    ]