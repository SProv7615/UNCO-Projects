from csv import reader
from markdown import markdown
from os.path import exists


def lorem(num_chars):
    text = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium quibusdam sit hic, ipsum labore commodi eligendi quos culpa maxime voluptate. Ad, voluptatem, esse! Quam accusantium minus sequi cumque minima quod odio accusamus assumenda dolorem consequuntur esse alias nisi, explicabo error! Dolores blanditiis adipisci laboriosam quo sequi nostrum consectetur recusandae illo sed molestias laborum, ullam modi doloremque. Facilis nulla iure odit accusamus. Doloremque voluptatibus repudiandae, beatae temporibus odit suscipit eius facere dolores quibusdam perspiciatis exercitationem velit porro cupiditate repellendus et tempora dolorem, sapiente, debitis cum nihil sunt. Illo perspiciatis cumque qui quia quam quibusdam doloribus fugiat porro, soluta esse nesciunt itaque? Blanditiis, voluptate, voluptates iure iste aut maxime perferendis aliquid, odit doloribus sapiente temporibus ad mollitia consequuntur, alias totam tenetur ut. Accusantium voluptas temporibus, ea a impedit.'''
    return text[:num_chars]


def card_data(title="Random Card", body=lorem(400), color='bg-primary', width='col-lg-12'):
    return dict(title=title, body=body, color=color, width=width)


def news_data(title, body, color='bg-primary', width='col-lg-6'):
    return dict(title=title, body=body, color=color, width=width)


def cards_data():
    return [
                card_data(),
                card_data("Card Two",   lorem(150), "bg-warning", 'col-lg-2'),
                card_data("Card Three", lorem(350), "bg-success", 'col-lg-4'),
                card_data("Card Four",  lorem(500), "bg-danger", 'col-lg-6'),
            ]


def markdown_file_data(doc):
    doc = 'documents/' + doc
    if not exists(doc):
        text = '# 404 is for Losers!'
    else:
        text = markdown(open(doc).read())
    title = f'document - {doc}'
    return card_data(title, text, 'bg-primary', 'col-lg-12') 


def tabs_data():

    def options(i, tab, selected):
        if selected:
            return dict(name=f'tab{i}', header=tab['title'], body=tab['body'],
                        active='active', show='show', selected='true')
        else:
            return dict(name=f'tab{i}', header=tab['title'], body=tab['body'],
                        active='', show='', selected='false')
 

    def set_options(tabs):
        return [options(i, tab, i == 2) for i, tab in enumerate(tabs)]

    
def accordion_data():

    def render_card_body(i):
        return f'<h2>Hero Bio</h2><p>Strengths</p><p>Weaknesses</p>'

    def card_content(i, active):
        card = dict(id=i, title=f'Week {i+1}', body=render_card_body(i+1))
        if i == active:
            card['show'] = 'show'
            card['active'] = 'true'
        return card

    return [card_content(i, 0) for i in range(18)]