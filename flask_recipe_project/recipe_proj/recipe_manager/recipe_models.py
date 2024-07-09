from .recipe_db import db

class Recipe(db.Model):
    __tablename__='recipe'
    recipe_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(300), nullable=False)
    preparation_time = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.String(500), nullable=False)

    def __str__(self):
        return self.title


class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return self.name


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    def __str__(self):
        return self.name


class RecipeIngredient(db.Model):
    recipeingredient_id = db.Column(db.Integer, primary_key=True)
    recipe = db.Column(db.String, db.ForeignKey('recipe.title'))
    ingredient = db.Column(db.String, db.ForeignKey('ingredient.name'))
    quantity = db.Column(db.Integer)

    def __str__(self):
        return self.recipe


class RecipeCategory(db.Model):
    recipecategory_id = db.Column(db.Integer, primary_key=True)
    recipe = db.Column(db.String, db.ForeignKey('recipe.title'))
    category = db.Column(db.String, db.ForeignKey('category.name'))

    def __str__(self):
        return self.recipe