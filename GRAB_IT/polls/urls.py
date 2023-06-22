from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('add', views.add, name = "add"),
    path('index1', views.index1, name='index1'),
    path('index2', views.index2, name='index2'),
    path('add1', views.add1, name = 'add1'),
    path('add2', views.add2, name = 'add2'),
    path('add3', views.add3, name = 'add3'),
    path('add4', views.add4, name = 'add4'),
    path('thank', views.thank, name = 'thank')
]