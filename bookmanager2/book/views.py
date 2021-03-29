from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import BookInfo
def index(request):

    return HttpResponse('index')


