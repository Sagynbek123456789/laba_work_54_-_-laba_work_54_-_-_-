from django import forms


class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=50, label='Наименование')
    descriptions = forms.CharField(max_length=200, required=False, label='Описание')


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=50, label='Наименование')
    descriptions = forms.CharField(max_length=200, required=False, label='Описание')
    image = forms.URLField(label='Изображение')


class ValidationError:
    pass


#
# class TaskForm(forms.Form):
#     description = forms.CharField(max_length=60, required=True, label='Описание')
#     status = forms.ChoiceField(choices=status_choices, label='Статус')
#     date_of_completion = forms.DateField(required=False, label='Дата выполнения')
#
