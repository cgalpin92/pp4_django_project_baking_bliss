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
    TEASPOONS = "tsps"
    TABLESPOON = "tbsp"
    TABLESPOONS = "tbsps"
    FLUID_OUNCE = "fl oz"
    CUP = "cup"
    CUPS = "cups"
    GRAMS = "g"
    KILOGRAMS = "kg"
    LITERS = "l"
    MILLILITERS = "ml"
    CENTIMETERS = "cm"
    BLANK = " "
    UNIT_CHOICES = [
        (TEASPOON, "teaspoon"),
        (TEASPOONS, "teaspoons"),
        (TABLESPOON, "tablespoon"),
        (TABLESPOONS, "tablespoons"),
        (FLUID_OUNCE, "fluid ounce"),
        (CUP, "cup"),
        (CUPS, "cups"),
        (GRAMS, "grams"),
        (KILOGRAMS, "kilograms"),
        (LITERS, "liters"),
        (MILLILITERS, "milliters"),
        (CENTIMETERS, "centimeters"),
        (BLANK, " "),
    ]
    ingredient_name = models.ForeignKey(IngredientName, on_delete=models.CASCADE, related_name="ingredient_name")
    measurement = models.IntegerField(default=0)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default=GRAMS)

    def __str__(self):
        return f"{self.measurement}{self.unit} {self.ingredient_name} "


class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.category_name}"


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

    def __str__(self):
        return f"{self.recipe_name}"


class Comment(models.Model):

    NO_RATING = "No Rating"
    ONE_OUT_OF_FIVE = "1/5"
    TWO_OUT_OF_FIVE = "2/5"
    THREE_OUT_OF_FIVE = "3/5"
    FOUR_OUT_OF_FIVE = "4/5"
    FIVE_OUT_OF_FIVE = "5/5"
    
    RATING_CHOICES = [
        (NO_RATING, "No Rating"),
        (ONE_OUT_OF_FIVE, "1/5"),
        (TWO_OUT_OF_FIVE, "2/5"),
        (THREE_OUT_OF_FIVE, "3/5"),
        (FOUR_OUT_OF_FIVE, "4/5"),
        (FIVE_OUT_OF_FIVE, "5/5"),
    ]

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comment")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_commenter")
    comment_title = models.CharField(max_length=50, default="Recipe Comment")
    body = models.TextField()
    rating = models.CharField(max_length=10, choices=RATING_CHOICES, default=NO_RATING)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment_title} by {self.author}"