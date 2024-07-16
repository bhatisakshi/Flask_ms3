import os
import logging
from .token_verify import token_verification
from .auth_pb2 import AuthResponse
from .auth_pb2_grpc import AuthServiceServicer


"""
Create log directory
"""
project_directory = os.path.dirname(os.path.realpath(__file__))
directory_path = os.path.join(project_directory, "logs")
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

logging.basicConfig(
    filename=os.path.join(directory_path, "grpc_server.log"), level=logging.DEBUG
)


class AuthServiceServer(AuthServiceServicer):
    """
    Recieves the authentication request and generates response(success flag, user_id) 
    using the token_verification method and sends it back to the client.
    """
    def Authenticate(self, request, context):
        logging.info("Received authentication request.")
        if request.token:
            success, user_id = token_verification(request.token)
            
            if success:
                logging.info(f"Authentication successful, user_id: {user_id}!")
            else:
                logging.warning(f"Authentication unsuccessful, success: {success}!")
            return AuthResponse(success=success, user_id=user_id)

        else:
            print("errror")
            logging.warning("Token not provided in request.")
            return AuthResponse(success=False, user_id=0)
