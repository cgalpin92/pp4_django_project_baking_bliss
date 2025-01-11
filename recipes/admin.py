from django.contrib import admin
from .models import IngredientName, Ingredient, Category, Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('recipe_name', 'category', 'difficulty', 'status')
    search_fields = ['category']
    list_filter = ('difficulty','status')
    prepopulated_fields = {'slug': ('recipe_name',)}
    ordering = ['status']

@admin.register(Ingredient)
class IngredientAdmin(SummernoteModelAdmin):
    list_display = ('ingredient_name', 'measurement', 'unit')
    ordering = ('ingredient_name',)
    list_filter = ('ingredient_name',)

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('comment_title', 'recipe', 'author', 'approved')
    list_filter = ['rating']
    ordering = ['approved']

# Register your models here.
admin.site.register(IngredientName)
admin.site.register(Category)
#admin.site.register(Comment)
