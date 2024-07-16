from .recipe_db import db

class Recipe(db.Model):
    __tablename__='recipe'
    recipe_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(300), nullable=False)
    preparation_time = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.String(500), nullable=False)
    
    ingredients = db.relationship('Ingredient', secondary='recipe_ingredient', backref='recipes')
    categories = db.relationship('Category', secondary='recipe_category', backref='recipes')
    
    def __repr__(self):
        return f'<Recipe {self.title}>'


class Ingredient(db.Model):
    __tablename__='ingredient'
    ingredient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    recipes = db.relationship('Recipe', secondary='recipe_ingredient', backref='ingredients')

    def __repr__(self):
        return f'<Ingredient {self.name}>'


class Category(db.Model):
    __tablename__='category'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    recipes = db.relationship('Recipe', secondary='recipe_category', backref='categories')
    
    def __repr__(self):
        return f'<Category {self.name}>'


class RecipeIngredient(db.Model):
    __tablename__='recipe_ingredient'
    recipeingredient_id = db.Column(db.Integer, primary_key=True)
    recipe = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))
    ingredient = db.Column(db.Integer, db.ForeignKey('ingredient.ingredient_id'))
    quantity = db.Column(db.Integer)


class RecipeCategory(db.Model):
    __tablename__='recipe_category'
    recipecategory_id = db.Column(db.Integer, primary_key=True)
    recipe = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))
    category = db.Column(db.Integer, db.ForeignKey('category.category_id'))