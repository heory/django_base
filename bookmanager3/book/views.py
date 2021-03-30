from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import BookInfo


def create_book(request):
    book=BookInfo.objects.create(
        name='abc',
        pub_date= '2020-1-1',
        readcount=10,
    )
    return HttpResponse('create')

def shop(request,city_id,shop_id):
    # print(city_id,shop_id)
    query_params = request.GET
    # print(query_params)

    order = query_params.get('order')
    print(order)
    return HttpResponse('奇哥的餐馆')

def register(request):
    data = request.POST
    print(data)
    return HttpResponse('OK')