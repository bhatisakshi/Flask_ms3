from recipe_proj.recipe_manager.recipe_db import ma
from recipe_proj.recipe_manager.recipe_models import (
    Recipe,
    Ingredient,
    Category,
    RecipeIngredient,
    RecipeCategory,
)


class RecipeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
        load_instance = True
        include_fk = True


class IngredientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ingredient
        load_instance = True
        include_fk = True


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True
        include_fk = True


class RecipeIngredientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RecipeIngredient
        load_instance = True
        include_fk = True


class RecipeCategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RecipeCategory
        load_instance = True
        include_fk = True