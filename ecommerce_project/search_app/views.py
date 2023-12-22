from django.shortcuts import render
from ecommerce_app.models import Product
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.


def SearchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q', '')
        products =Product.objects.all().filter(Q(product_name__contains = query) | Q(product_description__contains = query))
        return render(request,'search.html',{'query':query,'products': products})