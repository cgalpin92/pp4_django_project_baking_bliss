from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import IngredientName, Ingredient, Category, Recipe

# Create your views here.
# def recipe(request):
#     return HttpResponse("The recipe page works!")

class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "recipes/index.html"


class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipes/recipe_list.html"