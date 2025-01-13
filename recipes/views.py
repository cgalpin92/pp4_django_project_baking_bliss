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

class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "recipes/index.html"


class RecipeList(generic.ListView):
    queryset = Recipe.objects.all().order_by('-created_on')
    template_name = "recipes/recipe_list.html"


def recipe_by_category(request, category):
    """
    fetches the category name selected and assigns it
    the variable category_selected
    """
    """
    exception is used in case a category does not exist in the database
    """
    try:
        category_selected = Category.objects.get(
            category_name__icontains=category)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))
    """
    filters all the recipes by category_selected
    """
    recipes = Recipe.objects.filter(category=category_selected)
    """
    returns the view to recipe_category.html
    """
    return render(
        request,
        "recipes/recipe_category.html",
        {
            "recipes": recipes,
        }
    )


@login_required
def recipe_by_author(request):
    """
    lists all the Recipes by the user signed into Baking Bliss
    """
    """
    @login_required decorator at the start ensures that only logged in
    users can access this associated URL
    """
    user = get_object_or_404(User, username=request.user)
    profile = Recipe.objects.filter(author=user).order_by('-created_on')
    return render(
        request,
        "recipes/recipe_user.html",
        {
            "user": user,
            "profile": profile
        }
    )


def recipe_detail(request, slug):
    """
    lists the recipe information along with the comments
    and comments form
    """
    """
    Based on the post_detail view in the walkthrough project
    """
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
                request, messages.SUCCESS,
                "Your comment has been submitted for approval"
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


@login_required
def recipe_upload(request):
    """
    view for users to upload a recipe to Baking Bliss
    """
    """
    @login_required decorator ensures only logged in
    users can upload recipes
    """
    if request.method == "POST":
        recipe_form = RecipeForm(data=request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify(recipe.recipe_name)
            recipe.save()
            recipe_form.save_m2m()
            """
            same_m2m() required to save all options to database
            """
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


@login_required
def comment_edit(request, slug, comment_id):
    """
    view to allow logged in users to edit their own comments
    """
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
            messages.add_message(request, messages.ERROR,
                                 'Error updating Comment!')
    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    view to allow only logged in users to delete their own comments
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Your comment has been deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')
    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
def recipe_edit(request, slug):
    """
    view to allow only logged in users to edit recipes they have uploaded
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == "POST":
        recipe_form = RecipeForm(data=request.POST, instance=recipe)
        if recipe_form.is_valid() and recipe.author == request.user:
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify(recipe.recipe_name)
            recipe.save()
            recipe_form.save_m2m()
            messages.add_message(request, messages.SUCCESS,
                                 'Your Recipe has been updated!')
            return HttpResponseRedirect(reverse('users_recipe'))
    else:
        recipe_form = RecipeForm(instance=recipe)
    return render(
        request,
        "recipes/recipe_edit.html",
        {
            "recipe_form": recipe_form
        }
    )


@login_required
def recipe_delete(request, recipe_id):
    """
    view to allow only logged in users to delete recipes they have uploaded
    """
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.author == request.user:
        recipe.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Your Recipe has been deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own recipe!')
    return HttpResponseRedirect(reverse('users_recipe'))
