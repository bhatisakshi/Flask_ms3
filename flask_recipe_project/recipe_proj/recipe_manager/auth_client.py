import os
import grpc
import logging
from recipe_proj.recipe_manager.grpc_config import auth_pb2
from recipe_proj.recipe_manager.grpc_config import auth_pb2_grpc

"""
Create log directory
"""
project_directory = os.path.dirname(os.path.realpath(__file__))
directory_path = os.path.join(project_directory, "logs")
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

logging.basicConfig(
    filename=os.path.join(directory_path, "grpc_client.log"), level=logging.DEBUG
)


def authenticate(token):
    """
    Calls the Authenticate RPC method on the server.
    """
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = auth_pb2_grpc.AuthServiceStub(channel)
        request = auth_pb2.AuthRequest(token=token)
        try:
            logging.info("Sending authentication request with token: %s", token)        
            response = stub.Authenticate(request)
            logging.info("Authentication response received: success=%s, user_id=%d", response.success, response.user_id)
            return response.success, response.user_id
        except grpc.RpcError as e:
            logging.error(f"gRPC error during authentication: {e}")
            raise


