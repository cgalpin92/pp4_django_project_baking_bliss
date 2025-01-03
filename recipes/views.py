from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from .models import IngredientName, Ingredient, Category, Recipe, Comment

# Create your views here.
# def recipe(request):
#     return HttpResponse("The recipe page works!")

#class CategoryList(generic.ListView):
    #queryset = Category.objects.all()
    #template_name = "recipes/index.html"

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipes/index.html"


def recipe_detail(request, slug):
    
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    ingredients = Ingredient.objects.all()

    
    comments = recipe.comment.all()

    return render(
        request,
        "recipes/recipe_details.html",
        {
            "recipe": recipe,
            "ingredients": ingredients,
            "comments": comments,
        }
    )

