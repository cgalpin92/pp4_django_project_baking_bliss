from . import views
from django.urls import path

urlpatterns = [
   # path('', views.CategoryList.as_view(),
    #name='home'),
 #   path('', views.RecipeList.as_view(), name='home'),
 #  path('', views.recipe_list, name='home'),
 #   path('categories/', views.CategoryList.as_view(), name='category'),
   path('', views.CategoryList.as_view(), name="home"),    
   path('all_recipes/', views.RecipeList.as_view(), name='recipes'),
   path('recipe_upload/', views.recipe_upload, name="recipe_upload"),
   path('<slug:slug>/', views.recipe_detail, name="recipe_detail"),
   path('<str:category>', views.recipe_by_category, name="recipe_category")
]