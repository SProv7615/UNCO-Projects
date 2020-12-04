from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from hero.views import HeroListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('heroes/', HeroListView.as_view(), name='hero_list'),
]
