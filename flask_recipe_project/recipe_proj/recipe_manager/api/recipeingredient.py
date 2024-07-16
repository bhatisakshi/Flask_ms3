from flask import request
from flask_restx import Resource, fields, Namespace
from recipe_proj.recipe_manager.schema.recipe_schema import RecipeIngredientSchema
from recipe_proj.recipe_manager.token_required import token_required
from recipe_proj.recipe_manager.recipe_models import RecipeIngredient
from recipe_proj.recipe_manager.recipe_db import db

recipeingredient_ns = Namespace(
    "recipeingredients", description="Recipeingredient Operations"
)

recipeingredient_schema = RecipeIngredientSchema()
recipeingredients_schema = RecipeIngredientSchema(many=True)

recipeingredient_model = recipeingredient_ns.model(
    "RecipeIngredient",
    {
        "recipeingredient_id": fields.Integer(
            readonly=True, description="Recipe Ingredient ID"
        ),
        "recipe": fields.String(required=True, description="Recipe Name"),
        "ingredient": fields.String(required=True, description="Ingredient Name"),
        "quantity": fields.Integer(required=True, description="Ingredient Quantity"),
    },
)


@recipeingredient_ns.route("/recipeingredient")
class RecipeIngredientList(Resource):
    """
    Endpoint for retrieving recipe ingredients list and creating new ones.
    """

    @recipeingredient_ns.doc(security="apikey")
    @recipeingredient_ns.marshal_list_with(recipeingredient_model)
    @token_required
    def get(self, user_id, success):
        """
        Get all Recipe-Ingredients.
        """

        recipeingredients = RecipeIngredient.query.all()
        return recipeingredients_schema.dump(recipeingredients)

    @recipeingredient_ns.doc(security="apikey")
    @recipeingredient_ns.expect(recipeingredient_model)
    @recipeingredient_ns.marshal_with(recipeingredient_model)
    @token_required
    def post(self, user_id, success):
        """
        Create a new Recipe-Ingredient.
        """
        new_recipeingredient = recipeingredient_schema.load(request.json)
        db.session.add(new_recipeingredient)
        db.session.commit()
        return recipeingredient_schema.dump(new_recipeingredient), 201


@recipeingredient_ns.route("/recipeingredient/<int:recipeingredient_id>")
class RecipeIngredientDetail(Resource):
    """
    Endpoint for retrieving, updating or deleting a Recipe-Ingredient.
    """

    @recipeingredient_ns.doc(security="apikey")
    @recipeingredient_ns.expect({"recipeingredient_id": fields.Integer()})
    @recipeingredient_ns.marshal_with(recipeingredient_model)
    @token_required
    def get(self, user_id, success, recipeingredient_id):
        """
        Get a Recipe-Ingredient by ID.
        """
        recipeingredient = RecipeIngredient.query.get(recipeingredient_id)
        if not recipeingredient:
            recipeingredient_ns.abort(404, "Recipe-Ingredient not found")
        return recipeingredient_schema.dump(recipeingredient)

    @recipeingredient_ns.doc(security="apikey")
    @recipeingredient_ns.expect(recipeingredient_model)
    @recipeingredient_ns.marshal_with(recipeingredient_model)
    @token_required
    def put(self, user_id, success, recipeingredient_id):
        """
        Update a Recipe-Ingredient by ID.
        """
        data = request.json
        recipeingredient = RecipeIngredient.query.get(recipeingredient_id)
        if not recipeingredient:
            recipeingredient_ns.abort(404, "Recipe-Ingredient not found")

        updated_recipeingredient = recipeingredient_schema.load(data, instance=recipeingredient_schema)
        db.session.commit()
        return recipeingredient_schema.dump(updated_recipeingredient), 200

    @recipeingredient_ns.doc(security="apikey")
    @recipeingredient_ns.expect({"recipeingredient_id": fields.Integer()})
    @token_required
    def delete(self, user_id, success, recipeingredient_id):
        """
        Delete a Recipe-Ingredient by ID.
        """
        recipeingredient = RecipeIngredient.query.get(recipeingredient_id)
        if not recipeingredient:
            recipeingredient_ns.abort(404, "Recipe not found")
        db.session.delete(recipeingredient)
        db.session.commit()
        return {"message": "Recipe-Ingredient deleted successfully"}, 204