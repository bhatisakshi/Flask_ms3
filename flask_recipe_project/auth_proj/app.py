import os
from flask import Flask
from flask_restx import Api
from datetime import timedelta
from flask_jwt_extended import JWTManager
from .authentication.auth_db import init_app 
from .authentication.api.login import login_ns
from .authentication.api.logout import logout_ns
from .authentication.api.register import register_ns

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY="auth",
    SQLALCHEMY_DATABASE_URI="sqlite:///auth.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)


init_app(app)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

ACCESS_EXPIRES = timedelta(hours=1)

app.config["JWT_SECRET_KEY"] = "helloworld"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
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
