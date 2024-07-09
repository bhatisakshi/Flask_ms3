# gRPC Servcie
This gRPC service acts as a communication layer between the Authentication service and the RecipeManager. It facilitates:
- Sending token verification request from RecipeManager(Client) 
- Recieving token verification request and returning response(success flag, user_id)
- Error handling and efficient logging for request - sending, recieving and exceptions


## Features
- User registration
- User login and logout
- Protected view for token verification
  
## Installation

### Prerequisites
- Python 3.10 or higher
- Virtual environment tool
- Authentication Service: 
Ensure you have a running instance of the authentication service accessible to this gRPC service. Specify any requirements for interacting with the authentication service (e.g., API endpoint URLs).
- Recipe Manager Service: 
Ensure you have a running instance of the recipe manager service accessible to this gRPC service. Specify any requirements for interacting with the recipe manager service (e.g., gRPC server addresses).
gRPC Libraries: Install the necessary gRPC libraries for Python: pip install grpcio grpcio-tools
Installation

**Clone the repository:**
```bash
git clone https://github.com/bhatisakshi/Flask_ms3.git
cd flask_recipe_proj/auth_proj/authentication
```

**Create and activate a virtual environment:**
```bash
virtualenv venv
source venv/bin/activate 
```

**Install the dependencies:**
```bash
pip install -r requirements.txt
```


## Project Setup

1. Run the application:
```bash
python auth_server.py
```
The application will be available at localhost:50051


## Proto Buffers (if applicable)
```bash
protoc --proto_path=./protos --python_out=build/gen src/foo.proto src/bar/baz./protos
```