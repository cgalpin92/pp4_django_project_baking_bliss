from django.contrib import admin
from .models import IngredientName, Ingredient, Category, Recipe

# Register your models here.
admin.site.register(IngredientName)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Recipe)
