from os.path import dirname, exists, join


def workshop_menu():
    return {
      "url": "/",
      "label": "View Workshop",
      "menu_items": [
        {
          "url": "/card",
          "label": "Card",
          "page": "card"
        },
        {
          "url": "/doc/README.md",
          "label": "README",
          "page": "doc"
        },
        {
          "url": "/table",
          "label": "Table",
          "page": "table"
        },
        {
          "url": "/tabs",
          "label": "Tabs",
          "page": "tabs"
        }
      ]
    }


def load_menu(page):
    menu = workshop_menu()
    if menu:
        for item in menu['menu_items']:
            if page.startswith(item['page']):
                item['active'] = 'active'
        return menu


def load_side_menu(page):
    menu = workshop_menu()
    if menu:
        for item in menu['menu_items']:
            if page.startswith(item['page']):
                item['active'] = 'active'
        return menu