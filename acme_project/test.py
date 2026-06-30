from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class ContestForm(forms.Form):
    title = forms.CharField(
        label='Название',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )
    
    description = forms.CharField(
        label='Описание',
        required=True,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40})
    )
    
    price = forms.IntegerField(
        label='Цена',
        required=True,
        validators=[
            MinValueValidator(10),
            MaxValueValidator(100)
        ],
        widget=forms.NumberInput(),
        help_text='Рекомендованная розничная цена',
    )
    
    comment = forms.CharField(label='Комментарий',
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40})
    )