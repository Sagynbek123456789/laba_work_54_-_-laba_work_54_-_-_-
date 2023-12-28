from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from webapp.models import Product, Category
from webapp.forms import ProductForm
from django.urls import reverse_lazy
from django.db.models import Count, Sum
from django.db.models import F

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


class CartView(TemplateView):
    template_name = 'carts/carts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carts = Cart.objects.annotate(total=F('quantity')*F('product__price'))
        context['carts'] = carts
        context['total'] = carts.aggregate(total=Sum(F('quantity')*F('product__price')))['total']
        return context


class ProductDeleteOfCartView(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Cart, product_id=kwargs['pk'])
        product.delete()
        return redirect('carts_view')