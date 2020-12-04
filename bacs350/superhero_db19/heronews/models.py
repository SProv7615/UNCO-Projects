from django.db import models
from django.urls import reverse

class NewsPost(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=30)
    article = models.CharField(max_length=500)
    
    def __str__(self):
        return "Article: "+ self.title +"/n Author: "+ self.author
    
#    def get_absolute_url(self):
#        return reverse('hero_detail', args=[str(self.id)])
