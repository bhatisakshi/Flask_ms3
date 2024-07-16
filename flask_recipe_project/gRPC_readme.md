# gRPC Servcie
This gRPC service acts as a communication layer between the Authentication service and the RecipeManager.


## Features
- Sending token verification request from RecipeManager(Client) 
- Recieving token verification request and returning response(success flag, user_id)
- Error handling and efficient logging for request - sending, recieving and exceptions


## Installation

### Prerequisites
- Python 3.10 or higher
- Virtual environment tool
- Authentication Service: 
Ensure you have a running instance of the authentication service accessible to this gRPC service.
- Recipe Manager Service: 
Ensure you have a running instance of the recipe manager service accessible to this gRPC service. 


**Clone the repository:**
```bash
git clone https://github.com/bhatisakshi/Flask_ms3.git
cd flask_recipe_proj/auth_proj/authentication
```

**Create and activate a virtual environment:**
```bash
For linux:
    virtualenv venv 
    source venv/bin/activate 
    
For windows:
    python -m venv venv
    .\venv\Scripts\activate
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