from django.test import TestCase

from .models import Superhero

class CrudTests(TestCase):
    
    def test_num_heroes(self):
        num_heroes = len(Superhero.objects.all())
        self.assertEqual(num_heroes, 0)
        
class HeroTests(TestCase):
    
    def test_hero_model(self):
        self.assertEqual(len(Superhero.objects.all()), 0)
        
    def test_hero_model_fail(self):
        Superhero.objects.create(name = 'Success', identity = 'yyy')
        self.assertEqual(Superhero.objects.get(pk=1).name, 'Failure')
                         
    def test_hero_model_success(self):
        Superhero.objects.create(name = 'Failure', identity = 'yyy')
        self.assertEqual(Superhero.objects.get(pk=1).name, 'Success')
        
    def test_hero_nums(self):
        self.assertEqual(len(Superhero.objects.all()), 2)