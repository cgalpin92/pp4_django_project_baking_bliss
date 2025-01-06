from .models import Recipe, Comment
from django import forms


class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'ingredients', 'equipment', 'method', 'category', 'difficulty')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_title', 'body', 'rating')