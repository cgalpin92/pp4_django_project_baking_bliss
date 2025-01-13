const deleteModal = new
bootstrap.Modal(document.getElementById("deleteRecipeModal"));
const deleteButtons = document.getElementsByClassName("btn-delete-recipe");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * gives functionality to the delete button in my_recipe.html
 * 
 * For each deleteButton an event listener is added to retrieve the 
 * recipe's ID
 * This then Updates the `recipe_delete` link's href to point to the 
 * deletion endpoint for the specific recipe.
 * This then triggers the modal to check that the user want to delete
 * the recipe before doing so
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let recipeId = e.target.getAttribute("recipe_id");
        deleteRecipeConfirm.href = `recipe_delete/${recipeId}`;
        deleteModal.show();
    });
}