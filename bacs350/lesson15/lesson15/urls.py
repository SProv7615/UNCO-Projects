from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('blog.urls')), # new
    path('hero/', include('hero.urls'))
]
