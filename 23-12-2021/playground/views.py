from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, query
from store.models import Order, Product, OrderItem

def home_welcome(request):
    return render(request, "welcome.html", {"name":"Sohel"})

def say_hello(request):
    productquery1 = Product.objects.filter(Q(unit_price__lt = 5) & ~Q(inventory__lt = 10))
    productquery2 = Product.objects.filter(title = F("collection__title"))
    productquery3 = Product.objects.filter(unit_price__gt = 10).order_by("unit_price", "-title")
    productquery4 = Product.objects.filter(unit_price__gt = 10).earliest("unit_price", "-title")
    productquery5 = Product.objects.filter(unit_price__gt = 10).order_by("unit_price", "-title")[5:11]
    #productquery4 returns an object, hence not iterable, have to change template
    return render(request, 'hello.html', {'name': 'Sohel', "products": list(productquery5)})

def say_hello2(request):
    querydict = Product.objects.values("id", "title", "collection__title")
    querytuple = Product.objects.values_list("id", "title", "collection__title")
    ordered = OrderItem.objects.values("product_id").distinct()
    ordered_items = Product.objects.filter(id__in = ordered).order_by("title")
    
    return render(request, "hello2.html", {"products": list(ordered_items)})

