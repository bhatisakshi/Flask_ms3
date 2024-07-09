from flask import request
from flask_restx import fields, Resource, Namespace
from recipe_proj.recipe_manager.token_required import token_required
from recipe_proj.recipe_manager.recipe_models import Category
from recipe_proj.recipe_manager.recipe_db import db

category_ns = Namespace("categories", description="Category Operations")

category_model = category_ns.model(
    "Category",
    {
        "category_id": fields.Integer(readonly=True, description="Category ID"),
        "name": fields.String(required=True),
    },
)


@category_ns.route("/category")
class CategoryList(Resource):
    """
    Endpoint for retrieving all categories or creating a new one.
    """

    @category_ns.doc(security='apikey')
    @category_ns.marshal_list_with(category_model)
    @token_required
    def get(self, user_id, success):
        """
        Get all Categories.
        """
        categories = Category.query.all()
        return categories

    @category_ns.doc(security='apikey')
    @category_ns.expect(category_model)
    @category_ns.marshal_with(category_model)
    @token_required
    def post(self, user_id, success):
        """
        Create a new Category
        """
        category_data = request.json
        category = Category(**category_data)
        db.session.add(category)
        db.session.commit()
        return category, 201


@category_ns.route("/category/<int:category_id>")
class CategoryDetail(Resource):
    """
    Endpoint for retrieving, updating or deleting a Category.
    """

    @category_ns.doc(security='apikey')
    @category_ns.expect({"category_id": fields.Integer()})
    @category_ns.marshal_with(category_model)
    @token_required
    def get(self, user_id, success, category_id):
        """
        Get category by ID.
        """
        category = Category.query.get(category_id)
        if not category:
            category_ns.abort(404, "Category not found")
        return category, 201

    @category_ns.doc(security='apikey')
    @category_ns.expect(category_model)
    @category_ns.marshal_with(category_model)
    @token_required
    def put(self, user_id, success, category_id):
        """
        Update category by ID.
        """
        category_data = request.json
        category = Category.query.get(category_id)
        if not category:
            category_ns.abort(404, "Category not found")
        category.name = category_data.get("name")
        db.session.commit()
        return category, 200

    @category_ns.doc(security='apikey')
    @category_ns.expect({"category_id": fields.Integer()})
    @token_required
    def delete(self, user_id, success,  category_id):
        """
        Delete category by ID.
        """
        category = Category.query.get(category_id)
        if not category:
            category_ns.abort(404, "Category not found")
        db.session.delete(category)
        db.session.commit()
        return "Deleted category successfully! ", 204
