from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test),
    path('check', views.check_bd),
    path('district', views.district_data),
    path('upazila', views.upazila_data),
    path('search', views.searchresult, name= 'search'),
]
