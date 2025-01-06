from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from .models import IngredientName, Ingredient, Category, Recipe, Comment, User
from .forms import RecipeForm, CommentForm

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
    
    recipes = Recipe.objects.filter(category)
    return render(
        request,
        "recipes/recipe_category.html",
        {
            "category": category,
            "recipes": recipes,
        }
    )
"""
def recipe_list(request):
    recipe_list = Recipe.objects.all()

    return render(
        request,
        "recipes/index.html",
        {
            "recipe_list": recipe_list
        }
    )
"""

def recipe_detail(request, slug):
    
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    ingredients = Ingredient.objects.all()
    comments = recipe.comment.all()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user 
            comment.recipe = recipe
            comment.save()

    comment_form = CommentForm()
    

    return render(
        request,
        "recipes/recipe_details.html",
        {
            "recipe": recipe,
            "ingredients": ingredients,
            "comments": comments,
            "comment_form": comment_form,
        }
    )


def recipe_upload(request):

    if request.method == "POST":
        recipe_form = RecipeForm(data=request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()

    recipe_form = RecipeForm()
        

    return render(
        request,
        "recipes/recipe_upload.html",
        {
            "recipe_form": recipe_form,
        }
    )