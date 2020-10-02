"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from pages.views import PageView, AboutView
from hero.views import SpidermanView, BatmanView, IronManView, WolverineView, DeadpoolView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', PageView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('spiderman', SpidermanView.as_view(), name='spiderman'),
    path('batman', BatmanView.as_view(), name='batman'),
    path('ironman', IronManView.as_view(), name='ironman'),
    path('wolverine', WolverineView.as_view(), name='wolverine'),
    path('deadpool', DeadpoolView.as_view(), name='deadpool'),
]

urlpatterns += staticfiles_urlpatterns()