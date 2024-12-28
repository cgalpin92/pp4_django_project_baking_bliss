from django.contrib import admin
from .models import IngredientName, Ingredient, Category

# Register your models here.
admin.site.register(IngredientName)
admin.site.register(Ingredient)
admin.site.register(Category)
