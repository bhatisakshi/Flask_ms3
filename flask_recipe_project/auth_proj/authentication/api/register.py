from flask import request
from flask_restx import fields, Namespace, Resource
from werkzeug.security import generate_password_hash
from auth_proj.authentication.auth_models import db
from auth_proj.authentication.auth_models import User

register_ns = Namespace("authentication", description="Authentication Endpoints")

# User schema for input validation
user_model = register_ns.model(
    "User",
    {
        "username": fields.String(required=True, description="Username"),
        "password": fields.String(required=True, description="Password"),
    },
)


@register_ns.route("/register", methods=["POST"])
class Register(Resource):
    """
    Endpoint for registering a user
    """

    @register_ns.expect(user_model)
    def post(self):
        data = request.json
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            return {"message": "Username and password are required"}, 400
        user = User.query.filter_by(username=username).first()
        if user is not None:
            return {"message": "User already exists"}, 400
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User registered successfully"}, 201
