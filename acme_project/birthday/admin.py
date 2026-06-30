from django.contrib import admin


from .models import Birthday

# ...и регистрируем её в админке:
admin.site.register(Birthday)
admin.site.empty_value_display = "Не задано"
