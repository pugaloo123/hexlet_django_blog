from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# def index(request):
#     context = {
#         'title': 'About',
#         'desc': 'This page about this web'
#
#     }
#     return render(request, 'article/index.html', context)

class IndexView(View):
    context = {
        'title': 'About',
        'desc': 'This page about this web'
    }
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
        # return render(request, 'article/index.html', context=kwargs)



