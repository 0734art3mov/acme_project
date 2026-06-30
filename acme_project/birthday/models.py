# birthday/models.py
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

# Импортируется функция-валидатор.
from .validators import real_age

BEATLES = {"Джон Леннон", "Пол Маккартни", "Джордж Харрисон", "Ринго Старр"}


class Birthday(models.Model):
    first_name = models.CharField("Имя", max_length=20)
    last_name = models.CharField(
        "Фамилия", max_length=20, help_text="Опциональное поле", blank=True
    )
    birthday = models.DateField("Дата рождения", validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)

    constraints = (
        models.UniqueConstraint(
            fields=("first_name", "last_name", "birthday"),
            name="Unique person constraint",
        ),
    )

    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse("birthday:detail", kwargs={"pk": self.pk})
