from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
# Create your views here.
# view
def index(request):

    ontext = {
        'name': 'double one'
    }
    return render(request,'book/index.html',context=context)
