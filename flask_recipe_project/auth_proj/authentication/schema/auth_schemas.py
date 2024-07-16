from auth_proj.authentication.auth_db import ma
from auth_proj.authentication.auth_models import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        # include_fk = True  