from django.contrib import admin
from .models import IngredientName, Ingredient, Category, Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    registers the Recipe model against the admin site
    and applies the Summernote features below through to the model
    """
    list_display = ('recipe_name', 'category', 'difficulty', 'status')
    search_fields = ['category']
    list_filter = ('difficulty','status')
    prepopulated_fields = {'slug': ('recipe_name',)}
    ordering = ['status']


@admin.register(Ingredient)
class IngredientAdmin(SummernoteModelAdmin):
    """
    registers the IngredientName model against the admin site
    and applies the Summernote features below through to the model
    """
    list_display = ('ingredient_name', 'measurement', 'unit')
    ordering = ('ingredient_name',)
    list_filter = ('ingredient_name',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    registers the Comment model against the admin site
    and applies the Summernote features below through to the model
    """
    list_display = ('comment_title', 'recipe', 'author', 'approved')
    list_filter = ['rating']
    ordering = ['approved']


# Register your models here.
admin.site.register(IngredientName)
admin.site.register(Category)
