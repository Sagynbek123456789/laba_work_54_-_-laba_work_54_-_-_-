from django import forms
from webapp.models import Category, Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'descriptions', 'price', 'image', 'quantity', 'category')
    # title = forms.CharField(max_length=50, label='Наименование')
    # descriptions = forms.CharField(max_length=200, label='Описание')
    # category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all())
    # price = forms.DecimalField(decimal_places=2, max_digits=7,  label='Стоимость')
    # image = forms.URLField(label='Изображение')
    # quantity = forms.IntegerField(label='остаток', min_value=0)

    def clean_title(self):
        title = self.cleaned_data['title']
        title_old = self.initial.get('title')
        if not title_old or title !=title_old:
            if Product.objects.filter(title=title).exists():
                raise forms.ValidationError('Продукт с таким названием существует')
            return title


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'address', 'telephone')