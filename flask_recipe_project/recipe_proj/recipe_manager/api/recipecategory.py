from flask import request
from flask_restx import fields, Resource, Namespace
from recipe_proj.recipe_manager.token_required import token_required
from recipe_proj.recipe_manager.recipe_models import RecipeCategory
from recipe_proj.recipe_manager.recipe_db import db

recipecategory_ns = Namespace("recipecategories", description="RecipeCategory Operations")

recipecategory_model = recipecategory_ns.model(
    "RecipeCategory",
    {
        "recipecategory_id": fields.Integer(
            readonly=True, description="Recipe Category ID"
        ),
        "recipe": fields.String(required=True, description="Recipe Name"),
        "category": fields.String(required=True, description="Category Name"),
    },
)


@recipecategory_ns.route("/recipecategory")
class RecipeCategoryList(Resource):
    """
    Endpoint for retrieving all Recipe Categories or creating a new Recipe Category
    """

    @recipecategory_ns.doc(security="apikey")
    @recipecategory_ns.marshal_list_with(recipecategory_model)
    @token_required
    def get(self, user_id, success):
        """
        Get all Recipe-Categories.
        """
        recipe_categories = RecipeCategory.query.all()
        return recipe_categories

    @recipecategory_ns.doc(security="apikey")
    @recipecategory_ns.expect(recipecategory_model)
    @recipecategory_ns.marshal_with(recipecategory_model)
    @token_required
    def post(self, user_id, success):
        """
        Create a new Recipe-Category.
        """
        recipecategory_data = request.json
        new_recipecategory = RecipeCategory(**recipecategory_data)
        db.session.add(new_recipecategory)
        db.session.commit()
        return new_recipecategory, 201


@recipecategory_ns.route("/recipecategory/<int:recipecategory_id>")
class RecipeCategoryDetail(Resource):
    """
    Endpoint view to retrieve, update, or delete a Recipe Category.
    """

    @recipecategory_ns.doc(security="apikey")
    @recipecategory_ns.expect({"recipecategory_id": fields.Integer()})
    @recipecategory_ns.marshal_with(recipecategory_model)
    @token_required
    def get(self, user_id, success, recipecategory_id):
        """
        Get a Recipe-Category by ID.
        """
        recipecategory = RecipeCategory.query.get(recipecategory_id)
        if not recipecategory:
            recipecategory_ns.abort(404, "Recipe Category not found")
        return recipecategory, 201

    @recipecategory_ns.doc(security="apikey")
    @recipecategory_ns.expect(recipecategory_model)
    @recipecategory_ns.marshal_with(recipecategory_model)
    @token_required
    def put(self, user_id, success, recipecategory_id):
        """
        Update a Recipe-Category by ID.
        """
        recipecategory_data = request.json
        recipecategory = RecipeCategory.query.get(recipecategory_id)
        if not recipecategory:
            recipecategory_ns.abort(404, "Recipe Category not found")
        recipecategory.recipe = recipecategory_data.get("recipe")
        recipecategory.category = recipecategory_data.get("category")
        db.session.commit()
        return recipecategory, 200

    @recipecategory_ns.doc(security="apikey")
    @recipecategory_ns.expect({"recipecategory_id": fields.Integer()})
    @token_required
    def delete(self, user_id, success, recipecategory_id):
        """
        Delete a Recipe-Category by ID.
        """
        recipecategory = RecipeCategory.query.get(recipecategory_id)
        if not recipecategory:
            recipecategory_ns.abort(404, "Recipe Category not found")
        db.session.delete(recipecategory)
        db.session.commit()
        return "Recipe Category deleted successfully", 204


