from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'About',
        'desc': 'This page about this web'

    }




    return render(request, 'article/index.html', context)