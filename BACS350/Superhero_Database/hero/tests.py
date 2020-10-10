from django.test import TestCase

from .models import Superhero

class CrudTests(TestCase):
    def test_Num_Heroes(self):
        num_heroes = len(Superhero.objects.all())
        self.assertEqual(num_heroes, 0)

class HeroTests(TestCase):
    def test_hero_model(self):
        self.assertEqual(len(Superhero.objects.all()), 0)
        
        def test_create(self):
            Superhero.objects.create('The Spainaird','Inigo Montoya')
            self.assertEqual(len(Superhero.objects.all()), 1)