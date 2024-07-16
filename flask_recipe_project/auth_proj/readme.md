# Flask Authentication Project
A simple authentication application built using Flask and Flask-Restx.<br> This project includes basic user authentication features.

## Features
- User registration
- User login and logout
- Protected view for token verification
  
## Installation

### Prerequisites
- Python 3.10 or higher
- Virtual environment tool

**Clone the repository:**
```bash
git clone https://github.com/bhatisakshi/Flask_ms3.git
cd flask_recipe_proj/auth_proj
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

1. Initialize the database:
```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head 
```
2. Run the application:
```bash
flask run
```
The application will be available at http://127.0.0.1:5000/

## Endpoints

### Authentication Endpoints
- POST /authentication/register: Register a new user
- POST /authentication/login: Log in a user
- POST /authentication/logout: Log out a user
- POST /authentication/protected: For verifying token


