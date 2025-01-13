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

  - Bootstrap and CSS have been used to make Baking Bliss a responsive website and to ensure that each screen can be viewed on different screensizes. Through the use of DevTools It has been successfully tested on a variety of devices;
    - Mobile < = 768px
    - Tablet > = 768px
    - Laptop > = 992px
    - Desktop > = 1200px

  - The website utilizes the Bootstrap Grid layout and Card component. The cards are used to display the Recipes, Categories, Comments and Comments form which are set to display vertically on smaller screens. As the screen gets larger the cards begin to display horizontally. The navigation button which takes the user back to either the Home screen or to view All Recipes is located under the page title on smaller screens and on larger screens to the right of the page in-line with the page title.

  - Within the Header the Navigation menu has used Bootstrap stying to appear as a burger icon on smaller screens, which expands when selected. On laptop screens (992px) and larger the menu displays horizontally beneath the Site Name.

  - The Summernote Form Fields within the Recipe Upload and Recipe Edit screens are styled through settings.py so that respond to the screen size.

-__Browser Compatibility Testing__

  - Baking Bliss has been successfully tested across a range of different browsers; Chrome, Edge, Firefox and Safari (on a mobile device). Within each browser I was able to register an account, log in, upload a recipe, view that recipe, edit that recipe and delete that recipe. All navigation items and buttons responded correctly.

-__Lighthouse Testing__

  - I can confirm that the colors and fonts chosen for each page are easy to read and accessible by running it through lighthouse in Chrome DevTools.


-__User Stories Testing__

-__Features Testing__

  - I have tested that the navigation bar is responsive in both mobile and desktop view.

  - I have tested that a user can register, sign in and sign out successfully with a message confirming this.

  - I have successfully uploaded a new recipe to Baking Bliss, it has appeared in all the correct locations in a greyed out style until I have approved it in the admin.html.

  - I have successfully edited and deleted a recipe from the recipe_user.html page.

  - I have successfully edited and deleted a comment from the recipe_details page.


### Validator Testing

-__HTML__

  - When passing the code through the official W3C validator the following errors occured due to either Bootstrap or Summernote styling:

    - base.html 
      - Error - The aria-controls attribute must point to an element in the same document.
      - This error was not resolved due to the element it is referring to is a bootstrap imported element for the navbar menu toggle on smaller screens.
      - Due to every page extending from base.html, this error re-occured for each page test.
    
    - about.html
      - Error - No p element in scope but a p end tag seen.
      - This error was not resolved due to the p element filtering through from Summernote editor on the admin site. I navigated to this content in Admin and checked that no remaining spaces were at the end of the content incase this resolved the issue, however it did not.
    
    recipe_detail.html
      - Warning - Element name o:p cannot be represented as XML 1.0
      - I believe this is a result of using Summernote to style the recipe method.

      - Error - Element o:p not allowed as a child of element p in this context
      - Again I believe this is a result of using Summernote to style the recipe method.

      - Error - No p element in the scope but a p end tag seen.
      - Again believe this is due to summernote customisation in the admin.

      - Error - Attribute comment_id not allowed on element button at this point.
      - This I believe relates to the javascript code for editing and deleting the comments. It allows for the specific comment to be identified. This was taken from the Walkthrough project.

      - Error - End tag main seen, but there were open elements.
      - can confirm that the structure is correct, this was due to taking the code to input into validator from the site's source code to avoid the use of DTL throwing errors.

      - Error - Unclosed element div
      - can confirm that the structure is correct, this was due to taking the code to input into validator from the site's source code to avoid the use of DTL throwing errors.
    
    recipe_user.html
      - Error - Attribute recipe_id not allowed on element button at this point.
      - Same error as in recipe_detail for comment_id - believe relates to the javascript code for editing and deleting the comments. It allows for the specific comment to be identified. The syntax for relating the javascript code to the element was taken from the Walkthrough project.
    
    recipe_edit.html
      - The following errors were due to Summnote styling within the recipe_upload form:
        - Bad value true for attribute hidden on element textarea.
        - Element style not allowed as child of element div in this context. (Suppressing further errors from this subtree.)
        - Duplicate attribute class.
        - Attribute cols not allowed on element div at this point.
        - Attribute rows not allowed on element div at this point.
        - Attribute width not allowed on element div at this point.
        - Attribute height not allowed on element div at this point.
        - Bad value 100% for attribute width on element iframe: Expected a digit but saw % instead.
        - The frameborder attribute on the iframe element is obsolete. Use CSS instead.
    
    logout.html, login.html, signup.html
      - Error - Attribute active not allowed on element a at this point.
      - Django all_auth input
    
    signup.html
      - Following errors are part of Django All_auth:
        - End tag p implied, but there were open elements.
        - Unclosed element span.
        - Stray end tag span.
        - No p element in scope but a p end tag seen.

-__CSS__

  - No errors were found when passing through the official (Jigsaw) validator

-__JavaScript__

  - Have run the javascript code through jshint.
  - Warnings have appeared but no errors.
  - The warnings have stated that the variables and syntaxes used are only available in ES6. I do not believe any action is required here as it is not affecting the running of my code 

-__Python__

  - I have run the code through the CI pep8 python linter and it has returned no errors.

### Bugs

  - __Fixed Bugs__

    - Editing Recipes

      - When building the function to edit a recipe recieved a TypeError code stating that the function was missing 1 required positional argument 'recipe_id'
      - I found this was due to when building the function I was passing both the slug and the recipe id. Only one of these was required due to both being unique to the recipe.
      - I resolved this through removing the recipe_id argument and just using the slug to identify the recipe that the user would like to edit.

      - When building the function to edit a recipe the form page was loading but without any of the existing information.
      - I had not added the if argument request = POST to the function
      - Once this was added the form loaded with the pre-populated data to enter

      - Once the pre-populated fields were loading I noticed that the HTML code was being filtered through to the text fields in the form.
      - Through testing different recipes (ones that have been loaded through the Admin site and ones uploaded through the front end form) I found that those loaded through the admin site were displaying the HTML code when editing the recipe. This was due to summernote being used to edit the recipes in the Admin site. Found documentation on Github suggesting to import summernote fields into forms.py.
      - Once summernote fields were imported into forms.py the HTML code was no longer showing. However the textfields were not responsive, taking up over the max-width of the page. Found further down in the documentation how to configure the width of the text fields by adding height and width configurations into settings.py. This resolved the issue.
    
    - Uploading recipes
      
      - When the recipe form was first created the ingredients fields were not updating to the database. After searching through the django documentation found that after running recipe.save()at the end of the recipe_upload view, an additional function of recipe_form.save_m2m() was required to save the many to many fields to the database

    - Delete Recipes

      - When building the function to delete a recipe an error of page not found
      - This was due to an incorrect url - the terminal stated it was looking for my_recipes/delete_recipe/30 - whereas I had set the url as delete_recipe/<slug:slug>.
      - I updated the url to 'my_recipes/recipe_delete/<int:recipe_id>/' and passed the recipe id as an argument into the function and removed the slug argument.
      - This resulted in an additional error of clean() got an unexpected keyword argument 'styles'.
      - Through searching online found this was a compatibility issue between Django Summernote and the Bleach library.
      - Following the steps online [https://stackoverflow.com/questions/73789407/django-summernote-clean-got-an-unexpected-keyword-argument-styles-in-djangof] I uninstalled the latest version of Blean and re-installed Bleach 3.3.1.
      - This resolved the issue and allowed the recipe to be deleted.

    - Editing and Deleting comments:

      - When following the steps to edit and delete the comments on a recipe page the buttons were not reponding to the mouse click.
      - The delete function was due to a typo within comment.js, once this was resolved the comment would delete when requested.
      - The comment issue was due to a missing id from the comment_body element. Once this was added the edit button would allow the user to update the comment.


  - __Unfixed Bugs__

    - Summernote Fields within Admin site.
      - Due to configuration of Summernote Text field in settings.py to fix issue of text field overspilling the page in the front end forms, the size and width of the fields have also changed withn the admin site. On a desktop they are not taking up with width of the page. However this is not affecting the functionality of the site and I have been unable to find an alternative solution at the present time.

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
      - To create conditional naviation menu items in the header dependent on if user is signed in (the Register, Login and Logout items).
      - To create messages in response to a user action, either login, logout, sign-up, comment on a recipe, update or delete a comment and upload a recipe.
      - To create the edit and delete buttons for editing or deleting comments on a recipe
      - For displaying comments at the bottom of a recipe and creating the comments form
      - Function based view for displaying the recipe page
      - Model fields for the Comments model
    - The walkthrough project provided guidance on what packages to install such as Django AllAuth, Summernote, Crispy forms and Whitenoise. 
  
  - Code for displaying the many to many field ingredients as multiple choice text boxes in form sourced from tutorial on Medium.com:
    - https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024
  
  - Guidance on the Django framework taken from Django documentation:
    - https://docs.djangoproject.com/en/4.2/ 
  
  - Guidance on the Bootstrap library, along with some responsive boostrap code taken from Bootstrap documentation:
    - https://getbootstrap.com/docs/4.6/getting-started/introduction/

  - Guidance for ordering the multiple choice checkboxes in the upload form taken from Stack Overflow:
    - https://stackoverflow.com/questions/55493825/how-to-sort-drop-downs-in-alphabetical-order-in-django

  - Guidance on django models and model fields taken from:
    - https://docs.djangoproject.com/en/4.2/ref/models/fields/#manytomanyfield
  
  - Guidance on how to access model Ingredient for model Recipe in recipe_detail view taken from Stack Overflow:
    - https://stackoverflow.com/questions/71126435/django-models-many-to-many-relationship-problem
    - https://stackoverflow.com/questions/47271339/access-many-to-many-field-within-django-template

  - Guidance on how to import Summernote fields into forms and later customise them to behave responsively taken from GitHub:
    - https://github.com/lqez/django-summernote?tab=readme-ov-file#form
  
  - Guidance on how to resolve a compatibility error when deleting a recipe taken from Stack Overflow:
    - https://stackoverflow.com/questions/73789407/django-summernote-clean-got-an-unexpected-keyword-argument-styles-in-djangof
  
  
  ### Content
  - The recipes used for testing and initial deployment were sourced from BBC Good Food:
    - https://www.bbcgoodfood.com/recipes/collection/baking-recipes?page=1

  - The color pallet for this site was taken from the bake this Happen blog:
    - https://www.bakethishappen.com/blog/5-brand-palettes-for-your-home-baking-business
  
### Media

  - The images used within this project were taken from Pexels.com:
    - https://www.pexels.com/search/baking/




