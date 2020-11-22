from django.shortcuts import render


# Create your views here.

def index(request):
    context = {'page_title': 'Index page',}
    return render(request, 'mainapp/index.html', context)


