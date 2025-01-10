# BAKING BLISS

## Intro

- Baking Bliss is a baking recipe sharing site for baking enthusiasts. 

### Roles of the site:
  - __The site user__ can view all approved recipes without creating an account or signing into the site. However, should they wish to contribute to the site by sharing recipes of their own or comment on other people's recipes they will need to create an account and sign in.

  - __The site owner__ can also accomplish the above however they also have access to the admin site where they can approve recipes uploaded by other users and comments made on recipes. From the admin site they can also ;
    - add new categories or delete old ones
    - add new ingredients or delete old ones
    - add new recipes or delete old ones
    - delete user accounts

## Models

- I have used a total of 5 Models within this Project:
  - IngredientName
    - This model is for creating the name of the ingredient (for example Self-Raising Flour) within the database. The superuser adds this ingredient which populates through to the Ingredient model via a Foreign Key.

  - Ingrendient
    - This model has in addition to the IngredientName Foreign Key field from IngredientName model, also encompaces the unit and the measurement. Again the superuser creates this in the admin, this then filters through to the Recipe Model which the user is able to access.

  - Category
    - This model is for creating the categories that the recipes can be filtered by in Index.html.

  - Recipe
    - This model is for building the recipe. The user is able to access this model's fields by the form to upload a recipe. This model has foreign key fields to the User model and Category model. It also has a many to many field to the Ingredient model as there can be many ingredients to many recipes.

  - Comment
    - This model, which was taken from the I Think I Blog walkthrough project stores the comments made by the user about the recipe they are viewing. It has a Foreign Key field to both the User model and the Recipe Model.

## User Experience Stories

## Design

## Features

### Existing Features

### Features left to Implement

## Testing

### Manual Testing

### Validator Testing

### Bugs

  - __Fixed Bugs__


  - __Unfixed Bugs__

## Deployment

## Credits

### Code

  - Some code and guidance for building the django project were taken from the I Think I Blog walkthrough project:
   - Code taken from walkthrough project:
    - To create conditional naviation menu in the header dependent on if user is signed in
    - To create messages in response to a user action, either login, logout, sign-up, comment on a recipe, update or delete a comment and upload a recipe.
    - To create the edit and delete buttons for editing or deleting comments on a recipe
    - For displaying comments at the bottom of a recipe and creating the comments form
    - Function based view for displaying the recipe page
    - Comments mode
  
  - Code for displaying the many to many field ingredients as multiple choice text boxes in form sourced from tutorial on Medium.com:
   - https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024

  - Guidance for ordering the multiple choice checkboxes in the upload form taken from Stack Overflow:
   - https://stackoverflow.com/questions/55493825/how-to-sort-drop-downs-in-alphabetical-order-in-django

  - Guidance on django models and model fields taken from:
   - https://docs.djangoproject.com/en/4.2/ref/models/fields/#manytomanyfield
  
  - Guidance on how to access model Ingredient for model Recipe in recipe_detail view takne from Stack Overflow:
   - https://stackoverflow.com/questions/71126435/django-models-many-to-many-relationship-problem
   - https://stackoverflow.com/questions/47271339/access-many-to-many-field-within-django-template
  
  ### Content
  - The recipes used for testing and initial deployment were sourced from BBC Good Food:
   - https://www.bbcgoodfood.com/recipes/collection/baking-recipes?page=1


  - The color pallet for this site was taken from the bake this Happen blog:
   - https://www.bakethishappen.com/blog/5-brand-palettes-for-your-home-baking-business
  


### Media

  - The images used within this project were taken from Pexels.com:
    - https://www.pexels.com/search/baking/




