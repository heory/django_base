from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
# Create your views here.
from django.views import View

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

def set_cookie(request):
    username=request.GET.get('username')
    response=HttpResponse('set_cookie')
    response.set_cookie('name',username)
    return response

def get_cookie(request):

    print(request.COOKIES)

    name=request.COOKIES.get('name')
    return HttpResponse(name)

def set_session(request):

    username=request.GET.get('username')

    user_id=1

    request.session['user_id']=user_id
    request.session['username']=username

    # request.session.clear()
    request.session.flush()

    return HttpResponse('set_session')

def get_session(request):

    user_id=request.session['user_id']
    username=request.session['username']

    content='{},{}'.format(username,user_id)

    return HttpResponse(content)

def login(request):
    print(request.method)

    if request.method=='GET':
        return HttpResponse('get逻辑')
    else:
        return HttpResponse('post逻辑')

class LoginView(View):

    def get(self,request):
        return HttpResponse('get get get')

    def post(self,request):
        return HttpResponse('post post post')

class OrderView(LoginRequiredMixin,View):

    def get(self,request):
        return HttpResponse('GET 订单页面')

    def post(self,request):
        return HttpResponse('POST 订单页面')