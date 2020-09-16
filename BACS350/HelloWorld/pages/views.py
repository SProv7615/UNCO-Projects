from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('<h1>Home<h1>')

# Create your views here.
