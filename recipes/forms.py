from .models import Recipe, Comment, Ingredient
from django import forms


class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'ingredients', 'other_ingredients', 'equipment', 'method', 'category', 'difficulty')

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),widget=forms.CheckboxSelectMultiple
    )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_title', 'body', 'rating')