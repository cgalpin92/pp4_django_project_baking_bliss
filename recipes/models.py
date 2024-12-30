from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class IngredientName(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="ingredient_author")
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Ingredient(models.Model):
    TEASPOON = "tsp"
    TABLESPOON = "tbsp"
    FLUID_OUNCE = "fl oz"
    CUP = "cup"
    GRAM = "g"
    KILOGRAM = "kg"
    LITER = "l"
    MILLILITER = "ml"
    CENTIMETER = "cm"
    UNIT_CHOICES = [
        (TEASPOON, "teaspoon"),
        (TABLESPOON, "tablespoon"),
        (FLUID_OUNCE, "fluid ounce"),
        (CUP, "cup"),
        (GRAM, "gram"),
        (KILOGRAM, "kilogram"),
        (LITER, "liter"),
        (MILLILITER, "milliter"),
        (CENTIMETER, "centimeter"),
    ]
    ingredient_name = models.ForeignKey(IngredientName, on_delete=models.CASCADE, related_name="ingredient_name")
    measurement = models.IntegerField(default=0)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default=GRAM)


class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)


class Recipe(models.Model):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"
    DIFFICULTY_CHOICES = [
        (EASY, "Easy"),
        (MEDIUM, "Medium"),
        (HARD, "Hard"),
    ]
    recipe_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_post")
    ingredients = models.ManyToManyField(Ingredient)
    equipment = models.TextField()
    method = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipe_category")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default=EASY)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
