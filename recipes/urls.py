from . import views
from django.urls import path

urlpatterns = [
   path('', views.CategoryList.as_view(), name="home"),    
   path('all_recipes/', views.RecipeList.as_view(), name='recipes'),
   path('recipe_upload/', views.recipe_upload, name="recipe_upload"),
   path('my_recipes/', views.recipe_by_author, name="users_recipe"),
   path('categories/<str:category>', views.recipe_by_category, name="recipe_category"),
   path('<slug:slug>/', views.recipe_detail, name="recipe_detail"),
   path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name="comment_edit"),
   path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name="comment_delete"),
   
   
]