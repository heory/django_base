from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
# Create your views here.
from book.models import BookInfo


def create_book(request):
    book=BookInfo.objects.create(
        name='abc',
        pub_date= '2020-1-1',
        readcount=10,
    )
    return HttpResponse('create')

def shop(request,city_id,mobile):
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

def json_(request):

    body=request.body
    # print(body)
    body_str=body.decode()
    print(body_str)
    print(type(body_str))
    body_dict= json.loads(body_str)
    print(body_dict)
    print(type(body_dict))
    return HttpResponse('json')
from django.http import HttpResponse,JsonResponse
def response_(request):

    # return HttpResponse('res',status=200)
    # info={
    #     'name':'hhy',
    #     'address': 'Wuhan',
    # }
    #
    # friends=[
    #     {'name':'he',
    #      'address':'wuchang'},
    #     {'name':'liao',
    #      'address':'jiangan'}
    # ]
    # data= json.dumps(friends)
    # response = HttpResponse(data)
    return redirect('https://www.baidu.com')