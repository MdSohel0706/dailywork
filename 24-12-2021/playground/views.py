from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Sum, Max, Min, Avg
from django.db.models import Q, F, query
from django.db.models import Value, Func, ExpressionWrapper
from django.db.models.functions import Concat
from store.models import Order, Product, OrderItem, Customer

from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


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
    queryset = Product.objects.only("id", "title")
    preloadqueryset = Product.objects.select_related('collection').all()
    prefetchqueryset = Product.objects.prefetch_related('promotions').all()
    nestedqueryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    last_five_order_details = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    
    return render(request, "hello2.html", {"iterobj": list(last_five_order_details)})

def say_hello3(request):
    #aggregate function
    result = Product.objects.aggregate(count = Count('id'), min_price = Min('unit_price'))
    no_of_products_in_collection_1 = Product.objects.filter(collection__id = 3).aggregate(Count('id'))
    #annotate function
    queryset = Product.objects.annotate(is_new = Value(True))
    queryset2 = Product.objects.annotate(new_id = F('id') + 1000)
    queryset3 = Customer.objects.annotate(
        full_name = Func(F('first_name'), Value(' '), F('last_name'), function = 'CONCAT')
    )
    alternativequeryset3 = Customer.objects.annotate(
        full_name = Concat("first_name", Value(" "), "last_name")
    )

    queryset4 = Customer.objects.annotate(
        no_of_orders = Count('order')
    )

    #ExpressionWrapper
    expression = ExpressionWrapper(F('unit_price') * 2.00, output_field=DecimalField())
    queryset5 = Product.objects.annotate(discounted_price = expression)

    return render(request, "hello3.html", {"result" : queryset5})

def say_hello4(request):
    queryset = TaggedItem.objects.get_tags_for(Product, 3)

    return render(request, "hello4.html", {"result" : queryset})

