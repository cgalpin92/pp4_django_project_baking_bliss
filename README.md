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

  -__Color Scheme__

  - There are 3 main colors used across the Baking Bliss site, with an additional 3 supporting colors. 

    - These 3 main colors are Coral, Cream and Brown and are used primarily for background colors and main content font.
      - The Header, Footer, Recipe Cards and forms have a cream background and these are consistent across all pages.
      - The Header and Footer font are brown, intending to be clear stand out catching the user's attention.
      - The menu items within the Header are in coral, again contrasting against the cream background and tying in with the rest of the color scheme.
      - On all pages the primary background color is coral to keep consistency.
      
    - The supporting 3 colors are lilac, blush and grey which are used for buttons and indicating content waiting for approval. They again stand out from the rest of the content idicating a purpose. 

  -__Typography__

  - The fonts Outfit, Comfortaa and Playfair Display are used across the Baking Bliss site. 
  - Outfit - This font is used for the site name only to make this stand out. The site name is also in uppercase, again to grab the users attention.
  - Comfortaa is used for the menu items, buttons and remaining headers. Its a slightly softer font to the site name but still stands out and grabs the users attention. 
  - Playfair Display is used for any text content, again differentiating it from headers and action items.


## Features

### Existing Features

-__Header and Navigation Bar__

  - The Header and Navigation Bar encompasses the Site Name and the menu. Its featured at the top of the page with the Site Name in large font. The menu is fully responsive, either located beneath the Site Name across the width of the header on larger screens, or when on smaller screens as a burger icon to the top left of the page, which expands vertically when checked. Within the menu there is also an additional dropdown menu called Account which expands vertically when checked and lists the menu items; Login and Register (when the user is logged out) and the user's Username, Upload a Recipe, My Recipes and Logout (when the user is logged in).

  - The Header has a cream background with brown font for the Site Name and coral font for the Menu Items. However the username is in a lilac font to differentiate this item from the rest of the clickable menu items, it is also an an indication to the user that they are signed in.

  - The Header and Menu are identical across all pages to keep consistency and to ensure that it is easy to navigate for the user. Its fully responsive depending on the screen size its viewed on.


-__Home Page__

  - The Home page displays a list of category cards. Each card includes an image relating to that category. There is also a button labelled All Recipes that the user can select to view all the recipes in one list.

  - The aim of this page is to initially filter the recipes so that the site user can select the category they are interested in, rather than being presented straight away with a list of recipes, giving them a better user experience.  


-__About Page__

  - The About page introduces the purpose of the site along with the site owner and why they created Baking Bliss. The same color scheme is used to provide consistance for the user. The page content consists of a mage of baking items, information about the site and a date a the bottom of the screen indicating when this was last updated.
  

-__All Recipes__

  - The All Recipes page lists all the Recipes regardless of category. The purspose of this page is to have one space where all the recipes are listed for the user.
  - If the recipe is still waiting on approval from the Site Owner then they recipe name is displayed in a light grey font and does not show the Category, Difficulty and Author and instead displays the text Awaiting approval in brown font. If the recipe is approved then the recipe title becomes the clickable link to the recipe details, however if the recipe is still waiting on approval the link is removed.
  - There is a button at the top of the page labelled Categories which takes the user back to the home page.
  

-__My Recipes__

  - The My Recipes page lists all the recipes by the signed in user. Each approved recipe is displayed on a cream card with coral font for the recipe name and lilac font for the approved status. For the unapproved recipes the recipe name is in a grey font with the status Awaiting approval in brown font.

  - This page is to allow the user to find their own recipes. They also have the ability to Edit and Delete their recipes from this page.

  - If the user does edit or delete a recipe they are notified with a message at the top of the page.

-__Recipe Details__

  - This page displays the recipe information.

    - Recipe:
      - The first card on the page is the Recipe Card. This encompasses all the information for the recipe; Ingredients, Equipment, Method. The section headers are in lilac font with the information content in brown font. 
    - Comments:
      - The second card on the page is the Comments Card. It displays all the comments made by users about the recipe. The Comments title is in lilac font with the comments in brown font.
      - If the user is logged in they have the ability to Delete and Edit their own comments via the corresponding buttons.
    - Comment Form:
      - The final card on the page is the Comment Form Card. This allows a logged in user to leave a comment about the recipe. It has a section for the comment title, comment body and star rating. When this comment is submitted it is initially in grey font until approved by the Site Owner. The rating number is also converted into number of stars for a better user experience.


-__Upload a Recipe__

  - This page is the form for users to upload a new recipe, or edit an existing recipe. 

    - New Recipe:
      - If the user selects Upload Recipe from the menu in the header they are taken to a new form with no pre-populated information. The form includes the following fields:
        - Recipe Name - Character Field
        - Ingredients - Checkboxes, the user can select as many as needed
        - Other Ingredients - A text field for the user to input any additional ingredients that are not listed above. The Site Owner can then input these into the database before they appove the recipe.
        - Equipment - Summernote Text Field - allows the user to style this information, for example as a list.
        - Method - Summernote Text Field - again allows the user to style this information, for example with bold headings for each steap.
        - Category - Drop down options list
        - Difficulty - Drop down options list with default set to Easy
      - At the bottom of the form is an Upload Recipe button which send the recipe off for approval. The user is then notified via a message at the top of the screen. The recipe will also appear in the Recipes List, appropriate Cateogry page and My Recipe page in a grey out awaiting approval format.
    
    - Edit a recipe:
      - If the user selects Edit Recipe from the My Recipe page they are taken to the Upload Recipe form, however the page title states Edit Recipe and the form fields are pre-populated with the existing information which the user can change. There is a update recipe button at the bottom of the form. The new information will then replace the old recipe information. 

-__Register__

  - The register page is accessed from the dropdown Account menu when the user is logged out. When taken to this page the user is presented with a form to enter a username, optional email address and a password, there is also information on requirements for the password. There is a button at the bottom of the page labelled Sign Up. This will register the user on the database.
  - At the top of the page there is a button which is labelled sign in and accompanied by the text "Already have an account? Then please sign in" to ensure that an pre-existing user does not try to sign up again.
  - Once registered a message appears at the top of the screen confirming to the user they have registered.

-__Login__

  -  The login page, access via the menu in the header, provides the user with the Username and Password fields to sign in. If they have not created an account yet they can select the Sign Up button which will take them to the Register Page. Once signed in a message appears at the top of the screen confirming to the user they have signed in. Their username also appears in the header menu within the accounts dropdown.

-__Log Out__

  - This page is also located via the menu in the header, when selecting this page the user is asked if they are sure they would like to sign out to give better user experience rather than just signing the user out. Once signed out a message appears at the top of the screen confirming to the user they have signed out.

-__Footer__

  - The footer is located at the bottom of the page and is in the same style as the header. It is same across all pages to keep consistency. The copyright information is located here.

### Features left to Implement

  - Message board thread for users to interact rather than just within the comments
  - A profile page for the user where they can update their username, email address and password
  - Ability to upload photos with the recipes
  - A dark mode toggle feature
  - Search function or filter so that users can search for recipes by ingredient or author

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

-__Responsiveness Testing__

  - Bootstrap and CSS have been used to make Baking Bliss a responsive website and to ensure that each screen can be viewed on different screensizes. It has been successfully tested on a variety of devices such as iPhone, iPad, Laptop and Desktop. 

  - The website utilizes the Bootstrap Grid layout and Card component. The cards are used to display the Recipes, Categories, Comments and Comments form which are set to display vertically on smaller screens. As the screen gets larger the cards begin to display horizontally. The navigation button which takes the user back to either the Home screen or to view All Recipes is located under the page title on smaller screens and on larger screens to the right of the page in-line with the page title.

  - Within the Header the Navigation menu has used Bootstrap stying to appear as a burger icon on smaller screens, which expands when selected. On laptop screens (992px) and larger the menu displays horizontally beneath the Site Name.

  - The Summernote Form Fields within the Recipe Upload and Recipe Edit screens are styled through settings.py so that respond to the screen size.



-__Browser Compatibility Testing__

 

-__Lighthouse Testing__

-__User Stories Testing__

-__Features Testing__




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




