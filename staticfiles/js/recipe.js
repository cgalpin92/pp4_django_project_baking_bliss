const deleteModal = new
bootstrap.Modal(document.getElementById("deleteRecipeModal"));
const deleteButtons = document.getElementsByClassName("btn-delete-recipe");
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let recipeId = e.target.getAttribute("recipe_id");
        deleteRecipeConfirm.href = `recipe_delete/${recipeId}`;
        deleteModal.show();
    });
}