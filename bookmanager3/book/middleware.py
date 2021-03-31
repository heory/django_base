from django.utils.deprecation import MiddlewareMixin

class TestMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        print('11111111每次请求前都会调用')

        # username = request.COOKIES.get('name')
        # if username is None:
        #     print('没有用户信息')
        # else:
        #     print('有用户信息')

    def process_response(self,request,response):
        print('111111每次响应前都会调用')
        return response

class TestMiddleWare2(MiddlewareMixin):

    def process_request(self,request):
        print('222每次请求前都会调用')

        # username = request.COOKIES.get('name')
        # if username is None:
        #     print('没有用户信息')
        # else:
        #     print('有用户信息')

    def process_response(self,request,response):
        print('222每次响应前都会调用')
        return response
