from flask import request
from flask_restx import Resource, fields, Namespace
from recipe_proj.recipe_manager.token_required import token_required
from recipe_proj.recipe_manager.recipe_models import Ingredient
from recipe_proj.recipe_manager.recipe_db import db

ingredient_ns = Namespace("ingredients", description="Ingredient Operations")

ingredient_model = ingredient_ns.model(
    "Ingredient",
    {
        "ingredient_id": fields.Integer(readonly=True, description="Ingredient ID"),
        "name": fields.String(required=True, description="Ingredient Name"),
        "quantity": fields.String("Ingredient Quantity"),
    },
)


@ingredient_ns.route("/ingredient")
class IngredientList(Resource):
    """
    Endpoint for retrieving all ingredients and creating a new one.
    """

    @ingredient_ns.doc(security="apikey")
    @ingredient_ns.marshal_with(ingredient_model)
    @token_required
    def get(self, user_id, success):
        """
        Get all ingredients.
        """
        ingredients = Ingredient.query.all()
        return ingredients

    @ingredient_ns.doc(security="apikey")
    @ingredient_ns.expect(ingredient_model)
    @ingredient_ns.marshal_with(ingredient_model)
    @token_required
    def post(self, user_id, success):
        """
        Create a new ingredient.
        """
        ingredient_data = request.json
        new_ingredient = Ingredient(**ingredient_data)  # Unpack data into model instance
        db.session.add(new_ingredient)
        db.session.commit()
        return new_ingredient, 201


@ingredient_ns.route("/ingredient/<int:ingredient_id>")
class IngredientDetail(Resource):
    """
    Endpoint for retrieving, updating, or deleting a specific ingredient.
    """

    @ingredient_ns.doc(security="apikey")
    @ingredient_ns.expect({"ingredient_id": fields.Integer()})
    @ingredient_ns.marshal_with(ingredient_model)
    @token_required
    def get(self, user_id, success, ingredient_id):
        """
        Get an ingredient by ID.
        """
        ingredient = Ingredient.query.get(ingredient_id)
        if not ingredient:
            ingredient_ns.abort(404, "Ingredient not found")
        return ingredient

    @ingredient_ns.doc(security="apikey")
    @ingredient_ns.expect(ingredient_model)
    @ingredient_ns.marshal_with(ingredient_model)
    @token_required
    def put(self, user_id, success, ingredient_id):
        """
        Update an ingredient by ID.
        """
        ingredient_data = request.get_json()
        ingredient = Ingredient.query.get(ingredient_id)
        if not ingredient:
            ingredient_ns.abort(404, "Ingredient not found")

        ingredient.name = ingredient_data.get("name")
        ingredient.quantity = ingredient_data.get("quantity")
        db.session.commit()
        return ingredient, 200

    @ingredient_ns.doc(security="apikey")
    @ingredient_ns.expect({"ingredient_id": fields.Integer()})
    @token_required
    def delete(self, user_id, success, ingredient_id):
        """
        Delete an ingredient by ID.
        """
        ingredient = Ingredient.query.get(ingredient_id)
        if not ingredient:
            ingredient_ns.abort(404, "Ingredient not found")

        db.session.delete(ingredient)
        db.session.commit()
        return "Ingredient deleted successfully", 204



