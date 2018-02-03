# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from digging.models import Products,Stock_Products


def landingpage(request):
    return render_to_response('index.html')
def newArrivals(request):
    products = list(Products.objects.filter().values_list('image', flat=True).distinct())
    return render(request, 'newarrivals.html', {'products': products})
def stockProducts(request):
    sproducts = list(Stock_Products.objects.filter().values_list('image', flat=True).distinct())
   # sproducts = Stock_Products.objects.all()
    return render(request, 'stockproducts.html', {'sproducts': sproducts})


# Create your views here.