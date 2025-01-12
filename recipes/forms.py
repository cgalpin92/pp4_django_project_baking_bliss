from .models import Recipe, Comment, Ingredient
from django import forms
from django_summernote.fields import SummernoteTextField, SummernoteTextFormField


class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'ingredients', 'other_ingredients', 'equipment', 'method', 'category', 'difficulty')

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all().order_by('ingredient_name'),widget=forms.CheckboxSelectMultiple)
    
    
    equipment = SummernoteTextFormField()
    method = SummernoteTextFormField()
    

    


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_title', 'body', 'rating')