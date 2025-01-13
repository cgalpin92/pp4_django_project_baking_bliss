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
    Displays a list of recipes filtered by the category
    selected 
    Displays an individual :model:`recipe.Recipe`
    related to :model:`category:Category`
    **Context**
    ``category selected``
        identifies the category selected from
        :model: `category_name:Category`
    ``recipes``
        renders the list of recipes filtered by
        category_selected
    **Template**
    :template: `recipes/recipe_category.html`
    """
    try:
        category_selected = Category.objects.get(
            category_name__icontains=category)
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


@login_required
def recipe_by_author(request):
    """
    Displays a list of recipes filtered by the logged in
    user
    Displays an instance of :model:`recipe.Recipe` related
    to :model:`user:User`
    **Context**
    ``user``
        authenticated user of :model:`user.User`.
    ``profile``
        An instance of :model: `recipe.Recipe` filtered
        by the authenticated user.
    **Template**
    :template: `recipe/recipe_user.html`
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
    Displays an individual :model:`recipe.Recipe`
    **Context**
    ``recipe``
        an instance of :model:`recipe.Recipe`.
    ``comments``
        All approved comments related to recipe.
    ``ingrediants``
        All ingredients related to recipe.
    ``comment_form``
        An instance of :form:`recipe.CommentForm`.
    **Template**
    :template: `recipe/recipe_details.html`
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
    Displays an instance :form:`recipe.RecipeForm`
    **Context**
    ``recipe_form``
        an instance of :form:`recipe.RecipeForm
        related to the recipe selected`.
    **Template**
    :template: `recipe/recipe_upload.html`
    """
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


@login_required
def comment_edit(request, slug, comment_id):
    """
    Displays an instance of :model:`comment.Comment`
    **Context**
    ``recipe``
        an instance of :model:`recipe.Recipe` related
        to Recipe.status and Recipe.slug.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`recipe.CommentForm`.
    **Template**
    :template: `recipe/recipe_details.html`
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
    Deletes an individual comment.
    **Context**
    ``recipe``
        an instance of :model:`recipe.Recipe` related
        to Recipe.status and Recipe.slug.
        to Recipe.status and Recipe.slug.
    ``comment``
        A single comment related to the post
    **Template**
    :template: `recipe/recipe_details.html`
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
    Displays an instance of :model:`recipe.Recipe`
    **Context**
    ``recipe``
        a single recipe related
        to Recipe.slug.
    ``recipe_form``
        An instance of :form:`recipe.RecipeForm`.
    **Template**
    :template: `recipe/recipe_edit.html`
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
    Deletes an individual recipe
    **Context**
    ``recipe``
        a single recipe related to the recipes unique id.
    **Template**
    :template: `recipe/recipe_user.html`
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
