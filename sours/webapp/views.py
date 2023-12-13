from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, Category


def products_view(request):
    products = Product.objects.exclude(quantity=0)
    return render(request, 'products_list.html', {'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', {'product': product})


def product_add_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'product_create.html', {'categories': categories})
    elif request.method == "POST":
        product = Product.objects.create(
            title=request.POST.get('title'),
            price=request.POST.get('price'),
            image=request.POST.get('image'),
            descriptions=request.POST.get('descriptions'),
            category_id=request.POST.get('category_id')
        )
        return redirect('product_view', pk=product.pk)


def category_add_view(request):
    if request.method == "GET":
        return render(request, 'category_create.html')
    elif request.method == "POST":
        Category.objects.create(
            title=request.POST.get('title'),
            descriptions=request.POST.get('descriptions')
        )
        return redirect('index')