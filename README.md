# BAKING BLISS

## Intro

- Baking Bliss is a recipe sharing platform for baking enthusiasts to share their favourite recipes, discover new ones and connect with other fellow bakers. 

  ### Roles of the site:
    - __The site user__ can discover new recipes without creating an account or signing into the site. However, in order to contribute to the site by sharing their own recipes oor commenting on other recipes and connecting with other bakers they will need to create an account and sign in.

    - __The site owner__ can also accomplish the above however they also have access to the admin site where they can approve recipes uploaded by other users and comments made on recipes. From the admin site they can also;
      - add new categories or delete old ones
      - add new ingredients or delete old ones
      - add new recipes or delete old ones
      - delete user accounts

## Models

- I have used a total of 6 Models within this Project:
  - IngredientName Model
    - This model is for creating the name of the ingredient (for example Self-Raising Flour) within the database. The Site Owner adds this ingredient within the Admin portal which populates through to the Ingredient model via a Foreign Key.

  - Ingrendient Model
    - The Ingredient model has a Foreign Key relationship to the IngredientName model, this is the Name field. There are also in addition to this field the Unit field and Measurement Field. Like with the IngredientName model, the Site Admin inputs this data from within the Admin portal which then filters through to the Recipe Model.

  - Category
    - This model is for creating the categories that the recipes can be filtered by in Index.html. 

  - Recipe
    - The Recipe model is for building the recipe post. The Site Owner is able to create these Recipe posts both from within the Admin portal and from the Recipe Upload Form. The user is only able to create Recipe Posts from the Recipe Upload Form. This model has multiple relationships with other models.
    
      - Foreign Key Relationships:
      
        - User Model - The author field has a Foreign Key relationship with the User model, a Recipe post can only have one author but one user can be the author of many Recipe posts. 
        - Category Model - The category field has a Foreign Key relationship with the Category Model, a Recipe post can only have one category, but a category can cover many recipes.
      
      - Many to Many Relationship:
      
        - Ingredient - The ingredients field has a many-to-many relationship with the Ingredient Model. Recipes can have many ingredients, and those ingredients can feature in many recipes. I chose to create this as a many to many relationship rather than just as a text field so that the site owner can have some autonomy over the ingredients used, for example someone couldnt enter beef mince for a mince pie recipe. It also allows for the possibility of the site filtering by Ingredient in the future, a text field would not allow for this.

  - Comment
    - This model, which was taken from the I Think I Blog walkthrough project stores the comments made by the user about the recipe they are viewing. It has a Foreign Key relationship to both the User model and the Recipe Model.

  - About
    - This model, also taken from the I Think I Blog walkthrough project sits within the about app. Its purpose is to the allow the Site Admin to input information about Baking Bliss for the end user to read. It has no relationships to other models.

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
      - Comments model
  
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




