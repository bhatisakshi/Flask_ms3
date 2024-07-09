from concurrent import futures
import grpc
from grpc_config.auth import AuthServiceServer
from grpc_config.auth_pb2_grpc import add_AuthServiceServicer_to_server


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    add_AuthServiceServicer_to_server(AuthServiceServer(), server)
    print("Server listening on port 50051 with TLS/SSL encryption")
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()