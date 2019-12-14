from django.shortcuts import render
from django.utils import timezone
from .models import BuildingProduct


def building_product_list(request):
    ordered_list = BuildingProduct.objects.order_by('expiration_date')
    return render(request, 'building_product/building_product_list.html', {'building_products': ordered_list})
