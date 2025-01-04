from . import views
from django.urls import path

urlpatterns = [
   # path('', views.CategoryList.as_view(),
    #name='home'),
    path('', views.RecipeList.as_view(), name='home'),
    path('categories/', views.CategoryList.as_view(), name='category'),
    path('<slug:slug>/', views.recipe_detail, name="recipe_detail"),
    
    path('category/<category>', views.category_recipes, name="recipe_category")
]