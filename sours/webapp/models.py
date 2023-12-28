from django.core.validators import MinValueValidator, DecimalValidator
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Наименование')
    descriptions = models.TextField(max_length=200, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Наименование')
    descriptions = models.TextField(max_length=200, null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, related_name='products',
                                 verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')
    price = models.DecimalField(decimal_places=2, max_digits=7,  verbose_name='Стоимость')
    image = models.URLField(verbose_name='Изображение')
    quantity = models.PositiveIntegerField(default=1, verbose_name='остаток')




class Cart(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='products',
                                verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Колличество')














# from django.core.validators import MinValueValidator
# from django.db import models
#
#
# # Create your models here.
# class Category(models.Model):
#     title = models.CharField(max_length=50, unique=True, verbose_name='Наименование')
#     descriptions = models.TextField(max_length=200, null=True, blank=True, verbose_name='Описание')
#
#
# class Product(models.Model):
#     title = models.CharField(max_length=50, unique=True, verbose_name='Наименование')
#     descriptions = models.TextField(max_length=200, null=True, blank=True, verbose_name='Описание')
#     category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, related_name='products',
#                                  verbose_name='Категория')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')
#     price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')
#     # quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name='Остаток')
#     image = models.URLField(verbose_name='Изображение')