from django.shortcuts import render, get_object_or_404
from webapp.models import Product


def products_view(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products_view.html', {'product': product})