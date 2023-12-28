from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from webapp.models import Product, Category
from webapp.forms import ProductForm
from django.urls import reverse_lazy

from webapp.models import Product, Cart


class ProductAddToCartView(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs['pk'])
        carts = Cart.objects.filter(product=product)
        if carts:
            cart = carts.first()
            if product.quantity > cart.quantity:
                cart.quantity += 1
                cart.save()
        else:
            if product.quantity > 0:
                Cart.objects.create(product=product, quantity=1)

        return redirect('index')

