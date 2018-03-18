# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from digging.models import Products,Stock_Products
from django.core.paginator import Paginator

def landingpage(request):
    return render_to_response('index.html')
def newArrivals(request):
    products = list(Products.objects.filter().values_list('image', flat=True).distinct())
    return render(request, 'newarrivals.html', {'products': products})
def stockProducts(request):
    page_no = request.GET.get('page', 1)
    sproducts = Stock_Products.objects.filter()
    paginator = Paginator(sproducts, 5)
    return render(request, 'stockproducts.html', {'sproducts': list(paginator.page(page_no))})
def Products(request):
    page_no = request.GET.get('page', 1)
    sproducts = Stock_Products.objects.filter()
    paginator = Paginator(sproducts, 5)
    try:
        data = list(paginator.page(page_no))
    except:
        data = []
    return render(request, 'products.html', {'sproducts': data})

