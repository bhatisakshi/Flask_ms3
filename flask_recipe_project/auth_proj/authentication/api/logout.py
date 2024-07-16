from flask import jsonify
from flask_restx import Namespace, Resource
from flask_jwt_extended import unset_jwt_cookies


logout_ns = Namespace("authentication", description="Authentication Endpoints")


@logout_ns.route("/logout", methods=["POST"])
class Logout(Resource):
    """
    Logout endpoint
    """

    @logout_ns.doc(security="apikey")
    def logout_with_cookies():
        response = jsonify({"msg": "logout successful"})
        unset_jwt_cookies(response)
        return response
