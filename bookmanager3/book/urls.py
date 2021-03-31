from django.urls import path,converters
from django.urls.converters import register_converter
class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self,value):
        return value

    def to_url(self,value):
        return value

register_converter(MobileConverter,'phone')

from book.views import create_book, shop, register, json_, response_

urlpatterns = [
    path('create/', create_book),
    path('<int:city_id>/<phone:mobile>/',shop),
    path('register/',register),
    path('json/',json_),
    path('res',response_)
]
