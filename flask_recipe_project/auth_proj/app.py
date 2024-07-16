from flask import Flask
from flask_restx import Api
from flask_admin import Admin
from flask_jwt_extended import JWTManager
from .authentication.auth_db import init_app
from .authentication.auth_config import Config
from .authentication.api.login import login_ns
from .authentication.api.logout import logout_ns
from .authentication.api.register import register_ns

app = Flask(__name__)
app.config.from_object(Config)
app.config["FLASK_ADMIN_SWATCH"] = "cerulean"

admin = Admin(app, name="microblog", template_mode="bootstrap3")

init_app(app)
jwt = JWTManager(app)

authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}}
api = Api(
    app,
    title="Authentication",
    version="1.0",
    authorizations=authorizations,
    security="apikey",
)

api.add_namespace(login_ns)
api.add_namespace(logout_ns)
api.add_namespace(register_ns)
