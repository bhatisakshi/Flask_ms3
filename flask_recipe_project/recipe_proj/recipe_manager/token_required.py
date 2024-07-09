from functools import wraps
from flask import abort, request


def token_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        from .auth_client import authenticate

        auth_header = request.headers.get("Authorization")
        #Error handling
        if not auth_header:
            abort(401, description="Missing authorization header")

        # Extract token from cookie
        token = auth_header.split()[1].strip()

        #Eror handling
        if not token:
            abort(401, description="Invalid token format")

        success, user_id = authenticate(token)

        #Error handling
        if not success:
            abort(401, description="Invalid token")

        #Pass user_id and success flag where decorator is used for storing user-wise data
        return func(*args, user_id=user_id, success=success, **kwargs) 
    
    return decorated_function
