from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from .models import IngredientName, Ingredient, Category, Recipe, Comment, User

# Create your views here.
# def recipe(request):
#     return HttpResponse("The recipe page works!")



class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipes/index.html"


class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "recipes/category.html"




def category_recipes(request, category):
    
    queryset = Recipe.objects.filter(
        category__name__contains = category
    )
    return render(
        request,
        "recipes/recipe_category.html",
        {
            "category": category,
            "recipe": recipe,
        }
    )



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

