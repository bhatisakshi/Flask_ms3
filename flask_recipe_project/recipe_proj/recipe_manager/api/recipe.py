from flask import request
from flask_restx import Resource, fields, Namespace
from recipe_proj.recipe_manager.schema.recipe_schema import RecipeSchema
from recipe_proj.recipe_manager.token_required import token_required
from recipe_proj.recipe_manager.recipe_models import Recipe
from recipe_proj.recipe_manager.recipe_db import db

recipe_ns = Namespace("recipes", description="Recipe Operations")

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)

recipe_model = recipe_ns.model(
    "Recipe",
    {
        "recipe_id": fields.Integer(readonly=True, description="Recipe ID"),
        "title": fields.String(required=True, description="Recipe Name"),
        "description": fields.String(required=True, description="Recipe Description"),
        "preparation_time": fields.Integer(
            required=True, description="Preparation Time"
        ),
        "instructions": fields.String(required=True, description="Instructions"),
    },
)


@recipe_ns.route("/recipe")
class RecipeList(Resource):
    """
    Endpoint for retrieving all recipes and creating a new one.
    """

    @recipe_ns.doc(security="apikey")
    @recipe_ns.marshal_with(recipe_model)
    @token_required
    def get(self, user_id, success):
        """
        Get all Recipes.
        """
        recipes = Recipe.query.all()
        return recipes_schema.dump(recipes)

    @recipe_ns.doc(security="apikey")
    @recipe_ns.expect(recipe_model)
    @recipe_ns.marshal_with(recipe_model)
    @token_required
    def post(self, user_id, success):
        """
        Create a new Recipe.
        """ 
        new_recipe = recipe_schema.load(request.json)
        db.session.add(new_recipe)
        db.session.commit()
        return recipe_schema.dump(new_recipe), 201


@recipe_ns.route("/recipe/<int:recipe_id>")
class RecipeDetail(Resource):
    """
    Endpoint for retrieving, updating, or deleting a specific Recipe.
    """

    @recipe_ns.doc(security="apikey")
    @recipe_ns.expect({"recipe_id": fields.Integer()})
    @recipe_ns.marshal_with(recipe_model)
    @token_required
    def get(self, user_id, success, recipe_id):
        """
        Get a recipe by ID.
        """
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            recipe_ns.abort(404, "Recipe not found")
        return recipe_schema.dump(recipe)

    @recipe_ns.doc(security="apikey")
    @recipe_ns.expect(recipe_model)
    @recipe_ns.marshal_with(recipe_model)
    @token_required
    def put(self, user_id, success, recipe_id):
        """
        Update a recipe by ID.
        """
        data  = request.json
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            recipe_ns.abort(404, "Recipe not found")

        updated_recipe = recipe_schema.load(data, instance=recipe)
        db.session.commit()
        return recipe_schema.dump(updated_recipe), 200

    @recipe_ns.doc(security="apikey")
    @recipe_ns.expect({"recipe_id": fields.Integer()})
    @token_required
    def delete(self, user_id, success, recipe_id):
        """
        Delete a recipe by ID.
        """
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            recipe_ns.abort(404, "Recipe not found")
        db.session.delete(recipe)
        db.session.commit()
        return {"message": "Recipe deleted successfully"}, 204
