from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, Category
from webapp.forms import ProductForm


def products_view(request):
    products = Product.objects.exclude(quantity=0).order_by('category__title', 'title')
    return render(request, 'products_list.html', {'products': products})


def products_definitely_category_view(request, category_title):
    products = Product.objects.exclude(quantity=0).filter(category__title=category_title).order_by('category__title',
                                                                                                   'title')
    return render(request, 'products_list.html', {'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', {'product': product})


def product_add_view(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'product_create.html', {'form': form})
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                title=form.cleaned_data.get('title'),
                price=form.cleaned_data.get('price'),
                image=form.cleaned_data.get('image'),
                descriptions=form.cleaned_data.get('descriptions'),
                category=form.cleaned_data.get('category'),
                quantity=form.cleaned_data.get('quantity')
            )
            return redirect('product_view', pk=product.pk)
        return render(request, 'product_create.html', {'form': form})


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":

        form = ProductForm(initial={'title': product.title, 'price': product.price, 'image': product.image,
                                    'descriptions': product.descriptions, 'category': product.category,
                                    'quantity': product.quantity})
        return render(request, 'product_create.html', {'form': form})
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.title = form.cleaned_data.get('title')
            product.price = form.cleaned_data.get('price')
            product.image = form.cleaned_data.get('image')
            product.descriptions = form.cleaned_data.get('descriptions')
            product.category = form.cleaned_data.get('category')
            product.quantity = form.cleaned_data.get('quantity')
            product.save()

            return redirect('product_view', pk=product.pk)
        return render(request, 'product_create.html', {'form': form})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, 'product_delete.html', {'product': product})
    elif request.method == "POST":
        product.delete()
        return redirect('index')



def category_add_view(request):
    if request.method == "GET":
        return render(request, 'category_create.html')
    elif request.method == "POST":
        Category.objects.create(
            title=request.POST.get('title'),
            descriptions=request.POST.get('descriptions')
        )
        return redirect('index')
