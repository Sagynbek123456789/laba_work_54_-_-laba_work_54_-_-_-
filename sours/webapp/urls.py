from django.urls import path
from .views.products_views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    category_add_view, ProductDeleteView
from webapp.views.cart_views import ProductAddToCartView, CartView, ProductDeleteOfCartView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='products_view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('products/add/', ProductCreateView.as_view(), name='product_add_view'),
    path('categories/add/', category_add_view, name='category_add_view'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update_view'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete_view'),
    path('products/<int:pk>/add_to_cart/', ProductAddToCartView.as_view(), name='product_add_to_cart_view'),
    path('carts/', CartView.as_view(), name='carts_view'),
    path('products/<int:pk>/delete_of_cart/', ProductDeleteOfCartView.as_view(), name='product_delete_of_cart_view')
]
