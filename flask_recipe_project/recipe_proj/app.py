import os
from flask import Flask
from flask_restx import Api
from .recipe_manager.recipe_db import init_app
from .recipe_manager.api.recipe import recipe_ns
from .recipe_manager.api.ingredient import ingredient_ns
from .recipe_manager.api.category import category_ns
from .recipe_manager.api.recipecategory import recipecategory_ns
from .recipe_manager.api.recipeingredient import recipeingredient_ns


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY="recipe",
    SQLALCHEMY_DATABASE_URI="sqlite:///recipe_manager.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
try:
    os.makedirs(app.instance_path)
except OSError:
    pass
init_app(app)

authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    app,
    title="Recipe Manager",
    version="1.0",
    authorizations=authorizations,
    security="apikey",
)

api.add_namespace(ingredient_ns)
api.add_namespace(recipe_ns)
api.add_namespace(category_ns)
api.add_namespace(recipeingredient_ns)
api.add_namespace(recipecategory_ns)


