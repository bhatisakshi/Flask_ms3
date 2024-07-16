from flask import request
from flask_restx import Resource, fields, Namespace
from recipe_proj.recipe_manager.schema.recipe_schema import IngredientSchema
from recipe_proj.recipe_manager.token_required import token_required
from recipe_proj.recipe_manager.recipe_models import Ingredient
from recipe_proj.recipe_manager.recipe_db import db

ingredient_ns = Namespace("ingredients", description="Ingredient Operations")

ingredient_schema = IngredientSchema()
ingredients_schema = IngredientSchema(many=True)

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
        return ingredients_schema.dump(ingredients)

    @ingredient_ns.doc(security="apikey")
    @ingredient_ns.expect(ingredient_model)
    @ingredient_ns.marshal_with(ingredient_model)
    @token_required
    def post(self, user_id, success):
        """
        Create a new ingredient.
        """
        data = request.json
        new_ingredient = ingredient_schema.load(data)
        db.session.add(new_ingredient)
        db.session.commit()
        return ingredient_schema.dump(new_ingredient), 201


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
        return ingredient_schema.dump(ingredient)

    @ingredient_ns.doc(security="apikey")
    @ingredient_ns.expect(ingredient_model)
    @ingredient_ns.marshal_with(ingredient_model)
    @token_required
    def put(self, user_id, success, ingredient_id):
        """
        Update an ingredient by ID.
        """
        data = request.json
        ingredient = Ingredient.query.get(ingredient_id)
        if not ingredient:
            ingredient_ns.abort(404, "Ingredient not found")

        updated_ingredient = ingredient_schema.load(data, instance=ingredient)
        db.session.commit()
        return ingredient_schema.dump(updated_ingredient), 200

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
