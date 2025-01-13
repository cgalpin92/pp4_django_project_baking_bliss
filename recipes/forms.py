from .models import Recipe, Comment, Ingredient
from django import forms
from django_summernote.fields import SummernoteTextField, SummernoteTextFormField


class RecipeForm(forms.ModelForm):
    """
    creates the Recipe Upload form
    It takes the recipe model and applies the fields
    to the rendered form. The ingredients, equipment and methods fields
    are given further styling by setting them as either a multiple choice field
    for the ingredients or by providing the summernoteTextFormField for the 
    equipment and method fields to give a better user experience.
    """
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'ingredients', 'other_ingredients', 'equipment', 'method', 'category', 'difficulty')

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all().order_by('ingredient_name'),widget=forms.CheckboxSelectMultiple)
    
    
    equipment = SummernoteTextFormField()
    method = SummernoteTextFormField()
    

class CommentForm(forms.ModelForm):
    """
    creates the Comment form
    It takes the Comment model and applies the fields
    to the rendered form.
    """
    class Meta:
        model = Comment
        fields = ('comment_title', 'body', 'rating')