from django.contrib import admin
from .models import IngredientName, Ingredient

# Register your models here.
admin.site.register(IngredientName)
admin.site.register(Ingredient)
