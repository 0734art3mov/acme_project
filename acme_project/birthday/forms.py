# birthday/forms.py
from django import forms
from django.core.exceptions import ValidationError

from .models import Birthday  # 👈 Импорт модели
from .validators import real_age

BEATLES = {"Джон Леннон", "Пол Маккартни", "Джордж Харрисон", "Ринго Старр"}


class BirthdayForm(forms.ModelForm):  # 👈 ModelForm
    class Meta:
        model = Birthday  # 👈 Указываем модель
        fields = "__all__"  # 👈 Все поля
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "birthday": "Дата рождения",
        }
        help_texts = {
            "last_name": "Необязательное поле",
        }

    # Валидатор вызывается автоматически из модели,
    # но можно и явно продублировать для формы:
    def clean_first_name(self):
        # Получаем значение имени из словаря очищенных данных.
        first_name = self.cleaned_data["first_name"]
        # Разбиваем полученную строку по пробелам
        # и возвращаем только первое имя.
        return first_name.split()[0]

    def clean(self):
        # Получаем имя и фамилию из очищенных полей формы.
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        # Проверяем вхождение сочетания имени и фамилии во множество имён.
        if f"{first_name} {last_name}" in BEATLES:
            raise ValidationError("Ты — не он!")
