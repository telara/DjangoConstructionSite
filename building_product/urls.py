from django.urls import path
from . import views


urlpatterns = [
    path('', views.building_product_list, name='building_product_list'),
]
