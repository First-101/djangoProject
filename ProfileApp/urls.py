from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('firstweb', views.firstweb, name='firstweb'),
    path('secondpage', views.secondpage, name='secondpage'),
    path('thirdpage', views.thirdpage, name='thirdpage'),
    path('hny', views.hny, name='hny'),
    path('record', views.record, name='record'),
    path('interests', views.interests, name='interests'),
    path('educationalRecord', views.educationalRecord, name='educationalRecord'),
    path('product', views.product, name='product'),
    path('shop', views.shop, name='shop'),
]
