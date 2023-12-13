from webapp import forms


def validate_description(value):
    if len(value) > 60:
        raise forms.ValidationError('Длина превышает 60 символов')
