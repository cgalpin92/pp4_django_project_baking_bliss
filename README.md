# BAKING BLISS

## Intro

- Baking Bliss is a recipe sharing platform for baking enthusiasts to share their favourite recipes, discover new ones and connect with other fellow bakers. 

  ### Roles of the site:
    - __The site user__ can discover new recipes without creating an account or signing into the site. However, in order to contribute to the site by sharing their own recipes or commenting on other recipes and connecting with other bakers they will need to create an account and sign in.

    - __The site owner__ can also accomplish the above however they also have access to the admin site where they can approve recipes and comments uploaded by other users. From the admin site they can also;
      - Add new categories or delete old ones
      - Add new ingredients or delete old ones
      - Add new recipes or delete old ones
      - Add new comments or delete old ones
      - Create and Delete user accounts
      - Update the About page information

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

## Technologies Used

### Languages Used:

  - HTML5
  - CSS3
  - Python
  - Javascript

### Frameworks, Libraries and Programs Used:

  - __Django__ 
      - The Djang python framework was used to build Baking Bliss website.

  - __Bootstrap__ 
      - The Bootstrap framework was used in the project to assist with the website's styling and responsiveness.

  - __Crispy Forms__ 
      - The Crispy Forms package was used within the project to render the recipe upload and comment forms.

  - __Django Summernote__
      - The django summernote package was used to allow formatting and styling within the admin site and recipe upload form.
  
  - __Django All Auth__
      - The All Auth package was used to provide authorisation to the Baking Bliss site so that the project could have role based functionality.
  
  - __Whitenoise__
      - The Whitenoise library was used within the project for serving static files due to Django not having a built in function for this whilst in Production (DEBUG set to False).

  - __Balsamiq wireframes__
      - The Balsamiq wireframes programm was used in the front end design of the site to map out how each page would appear on different screen sizes.

  - __Google Fonts__
      - Google fonts was used to import the fonts used within the project. These fonts were Outfit, Comfortaa and Playfair Display.

  - __Font Awesome__
      - Font awesome was used to add icons for aesthetic and UX purposes.


## Testing

### Manual Testing



### Validator Testing

### Bugs

  - __Fixed Bugs__


  - __Unfixed Bugs__

## Deployment

### Forking:
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate this [GitHub Repository](https://github.com/cgalpin92/pp4_django_project_baking_bliss)
2. At the top of the Repository just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Cloning:
1. Log in to GitHub and locate this [GitHub Repository](https://github.com/cgalpin92/pp4_django_project_baking_bliss)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

For further information and a more detailed explaination, click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)


### Heroku
This project was deployed using Heroku.

- __Steps for deployment:__
    - Fork or clone this repository
    - Create a new Heroku app
        - Login to Heroku and select __Create New App__
        - Create app name
        - Select your __region__
        - Select __Create App__
    - Change Heroku Settings
        - Select __Settings__
        - Scroll down to __Config Var__ section and select __reveal config var__
        - Enter the following information into the __Key__ and __value__ inputs:
            - __Key:__ COLLECT_STATIC_FILES
            - __Value:__ 1
        - Select __Add__    
    - Link the Heroku app to the repository:
        - Select __Deploy__ from the top of the page.
        - Scroll down to __Deployment method__
        - Select __GitHub. Connect to GitHub__
        - Enter your repository name and click search
        - Select connect next to your repository name
    - Click on __Deploy__


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




