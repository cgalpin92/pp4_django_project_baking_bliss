from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class IngredientName(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="ingredient_author")
    approved = models.BooleanField(default=False)