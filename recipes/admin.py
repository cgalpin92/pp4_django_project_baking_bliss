from django.contrib import admin
from .models import IngredientName, Ingredient, Category, Recipe
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('recipe_name', 'category', 'difficulty')
    search_fields = ['category']
    list_filter = ('difficulty',)
    prepopulated_fields = {'slug': ('recipe_name',)}

# Register your models here.
admin.site.register(IngredientName)
admin.site.register(Ingredient)
admin.site.register(Category)
