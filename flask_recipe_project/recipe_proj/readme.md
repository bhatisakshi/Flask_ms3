# Flask Recipe-Manager Project
A simple Recipe Manager application built using Flask and Flask-Restx.<br> This project demonstrates basic CRUD operations and includes user authentication features for:
- Recipes
- Categories
- Ingredients
- Recipe-Ingredients
- Recipe-Categories 


## Features
- User Authorization using Bearer Token
- Recipe CRUD Operations - GET(All), POST, GET(One), PUT, DELETE
- Category CRUD Operations - GET(All), POST, GET(One), PUT, DELETE
- Ingredient CRUD Operations - GET(All), POST, GET(One), PUT, DELETE
- Recipe-Category CRUD Operations - GET(All), POST, GET(One), PUT, DELETE
- Recipe-Ingredient CRUD Operations - GET(All), POST, GET(One), PUT, DELETE 

## Installation

### Prerequisites
- Python 3.10 or higher
- Virtual environment tool

**Clone the repository:**
```bash
git clone https://github.com/bhatisakshi/Flask_ms3.git
cd flask_recipe_proj/recipe_proj
```

**Create and activate a virtual environment:**
```bash
virtualenv venv
source venv/bin/activate 
```

**Install the dependencies:**
```bash
pip install -r requirements.txt
```


## Project Setup

1. Initialize the database:
```bash
flask init-recipe-db
```
2. Run the application:
```bash
flask run --port 5001
```
The application will be available at http://127.0.0.1:5001/


## RecipeManager Endpoints

**Recipe**
- GET /recipes/recipe: List all recipes
- POST /recipes/recipe: Create a new recipe
- GET /recipes/recipe/int:recipe_id: Fetch a recipe by recipe_id
- PUT /recipes/recipe/int:recipe_id: Update a recipe by recipe_id
- DELETE /recipes/recipe/int:recipe_id: Delete a recipe by recipe_id

**Category**
- GET /categories/category: List all categories
- POST /categories/category: Create a new category
- GET /categories/category/int:category_id: Fetch a category by category_id
- PUT /categories/category/int:category_id: Update a category by category_id
- DELETE /categories/category/int:category_id: Delete a category by category_id

**Ingredient**
- GET /ingredients/ingredient: List all ingredients
- POST /ingredients/ingredient: Create a new ingredient
- GET /ingredients/ingredient/int:ingredient_id: Fetch a ingredient by ingredient_id
- PUT /ingredients/ingredient/int:ingredient_id: Update a ingredient by ingredient_id
- DELETE /ingredients/ingredient/int:ingredient_id: Delete a ingredient by ingredient_id

**RecipeCategory**
- GET /recipecategories/recipecategory: List all recipecategories
- POST /recipecategories/recipecategory: Create a new recipecategory
- GET /recipecategories/recipecategory/int:recipecategory_id: Fetch a recipecategory by recipecategory_id
- PUT /recipecategories/recipecategory/int:recipecategory_id: Update a recipecategory by recipecategory_id
- DELETE /recipecategories/recipecategory/int:recipecategory_id: Delete a recipecategory by recipecategory_id

**Recipe**
- GET /recipeingredients/recipeingredient: List all recipeingredients
- POST /recipeingredients/recipeingredient: Create a new recipeingredient
- GET /recipeingredients/recipeingredient/int:recipeingredint_id: Fetch a recipeingredient by recipeingredint_id
- PUT /recipeingredients/recipeingredient/int:recipeingredint_id: Update a recipeingredient by recipeingredint_id
- DELETE /recipeingredients/recipeingredient/int:recipeingredint_id: Delete a recipeingredient by recipeingredint_id

## Testing
To run the tests, use pytest:
```bash
pytest
```
