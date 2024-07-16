import jwt
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import set_access_cookies
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from flask_restx import abort, fields, Namespace, Resource
from auth_proj.authentication.auth_models import User
from auth_proj.authentication.schema.auth_schemas import UserSchema


user_schema = UserSchema()
users_schema = UserSchema(many=True)

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
        user_data = user_schema.load(request.json)

        response = jsonify({"msg": "login successful"})

        user = User.query.filter_by(username=user_data.username).first()
        if user is None or not check_password_hash(user.password, user_data.password):
            return {"message": "Invalid username or password"}

        # Generate access token on successful login
        payload = {"user_id": user.id, "username": user_data.username}
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
        auth_header = request.headers.get("Authorization")
        # Error handling
        if not auth_header:
            abort(401, description="Missing authorization header")

        # Extract token from cookie
        token = auth_header.split()[1].strip()

        # Eror handling
        if not token:
            abort(401, description="Invalid token format")

        if token:
            try:
                # Access the identity of the current user with get_jwt_identity
                # Manually decode the JWT token using secret key (replace with your logic)
                secret_key = "helloworld"
                decoded_data = jwt.decode(token, secret_key, algorithms=["HS256"])

                # Get user_id from decoded data(payload)
                current_user = decoded_data.get("sub", {}).get("username", 0)
                return {"message": f"Hi! Welcome back {current_user}"}, 200
            # Exception Handling:
            except jwt.ExpiredSignatureError:
                return {"message": "Couldn't extract user id from token"}
