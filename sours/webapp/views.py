from django.shortcuts import render
from webapp.models import Product

def products_view(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})