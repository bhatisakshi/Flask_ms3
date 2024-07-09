from flask import request, jsonify
from flask_restx import fields, Namespace, Resource
from werkzeug.security import check_password_hash
from auth_proj.authentication.auth_models import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import set_access_cookies

login_ns = Namespace("authentication", description="Authentication Endpoints")

# User schema for input validation
user_model = login_ns.model(
    "User",
    {
        "username": fields.String(required=True, description="Username"),
        "password": fields.String(required=True, description="Password"),
    },
)


@login_ns.route("/login", methods=["POST"])
class Login(Resource):
    """
    Login endpoint
    """

    @login_ns.expect(user_model)
    def post(self):
        data = request.json
        username = data.get("username")
        password = data.get("password")

        response = jsonify({"msg": "login successful"})

        user = User.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password, password):
            return {"message": "Invalid username or password"}, 401  # Unauthorized

        # Generate access token on successful login
        payload = {"user_id": user.id, "username": username}
        access_token = create_access_token(identity=payload)
        set_access_cookies(response, access_token)
        return {"message": "Login successful", "access_token": access_token}, 200


@login_ns.route("/protected", methods=["GET"])
class ProtectedResource(Resource):
    """
    Protected endpoint requiring a valid access token
    """

    @login_ns.doc(security="apikey")
    @jwt_required()
    def get(self):
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        return {"message": f"Hi! Welcome back"}, 200
