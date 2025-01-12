from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from .models import IngredientName, Ingredient, Category, Recipe, Comment, User
from .forms import RecipeForm, CommentForm


# Create your views here.

"""
This class view lists all the Categories and displays them in Index.html
"""

class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "recipes/index.html"

"""
This class view lists all the Recipes, ordering them by newest recipe first
and displays them in recipe_list.html
"""
class RecipeList(generic.ListView):
    queryset = Recipe.objects.all().order_by('-created_on')
    template_name = "recipes/recipe_list.html"

"""
This function view lists all the Recipes under specific categories.
It identifies the category name selected in Index.html and filters the Recipe
Model by that category. It uses an exception in the case that a user enters a 
category into the URL that does not exist in the database.
"""
def recipe_by_category(request, category):
    
    try:
        category_selected = Category.objects.get(category_name__icontains=category)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))
    recipes = Recipe.objects.filter(category=category_selected)
    
    return render(
        request,
        "recipes/recipe_category.html",
        {
            "recipes": recipes,
        }
        
    )

"""
This function view lists all the Recipes by the user signed into Baking Bliss.
The @login_required decorator at the start ensures that only users logged in can 
access this associated URL, if the are not then they are re-directed to the login
page. Once logged in they will be automatically returned to the recipe_user.html page
"""
@login_required
def recipe_by_author(request):
    
    user = get_object_or_404(User, username=request.user )
    profile = Recipe.objects.filter(author=user).order_by('-created_on')

    return render(
        request,
        "recipes/recipe_user.html",
        {
            "user": user,
            "profile": profile
        }
    )

"""
This function view is the recipe details page.
It filters the Recipe model by only approved recipes
The function also fetches all the Ingredients objects
so that they can be looped through in the page the Ingredient
model has a many to many relationship with the Recipe Model.
The comment form is created below and displayed within the Recipe
Details view
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
            messages.add_message(
                request, messages.SUCCESS, "Your comment has been submitted for approval, you can still edit or delete it below"
            )

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

"""
This function view is the Recipe Upload form.
It connected to the RecipeForm class in forms.py
It will save the information provided to the server once all the information
has been added. A message will then display to the user confirming that the recipe
has been sent and in approval stage.

The @login_required decorator at the start ensures that only users logged in can 
access this associated URL, if the are not then they are re-directed to the login
page. Once logged in they will be automatically returned to the recipe_upload.html page
"""
@login_required
def recipe_upload(request):

    if request.method == "POST":
        recipe_form = RecipeForm(data=request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify(recipe.recipe_name)
            recipe.save()
            recipe_form.save_m2m()
            
            messages.add_message(
                request, messages.SUCCESS,
                "Your Recipe has been submitted for approval"
            )
            

    recipe_form = RecipeForm()   

    return render(
        request,
        "recipes/recipe_upload.html",
        {
            "recipe_form": recipe_form,
        }
    )

"""
This function view lists allows users to edit their own comments.
A message will then display to the user confirming that the comment has 
been updated if successfull or stating an Error if not.
The @login_required decorator at the start ensures that only users logged in can 
access this associated URL, if the are not then they are re-directed to the login
page. Once logged in they will be automatically returned to the recipe_details.html page
"""
@login_required
def comment_edit(request, slug, comment_id):

    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)

        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()

            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating Comment!')
    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))

"""
This function view allows users to delete their own comments.
A message will then display to the user confirming that the comment has 
been deleted if successfull or stating an Error if not.
The @login_required decorator at the start ensures that only users logged in can 
access this associated URL, if the are not then they are re-directed to the login
page. Once logged in they will be automatically returned to the recipe_details.html page
"""
@login_required
def comment_delete(request, slug, comment_id):

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Your comment has been deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')
    
    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
def recipe_edit(request, slug):

    #queryset = Recipe.objects.all()
    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method == "POST":

        recipe_form = RecipeForm(data=request.POST, instance=recipe)
        if recipe_form.is_valid() and recipe.author == request.user:
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify(recipe.recipe_name)
            recipe.save()
            recipe_form.save_m2m()


            messages.add_message(request, messages.SUCCESS, 'Your Recipe has been updated!')
       
            return HttpResponseRedirect('recipe_user')
    else:

        recipe_form = RecipeForm(instance=recipe)
    
    return render (
        request,
        "recipes/recipe_edit.html",
        {
            "recipe_form": recipe_form
        }
    )


