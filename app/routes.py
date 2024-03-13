from main import app, jwt
from flask import render_template
from flask_jwt_extended import jwt_required

# controlers
from controllers.user_controller import UserController

# API ROUTES

## PROTECTED 
@app.route("/api/v1/user/<nickname>", methods=["DELETE"])
@jwt_required()
def delete_user(nickname):
    return UserController.delete_user(nickname)

@app.route("/api/v1/user/<nickname>", methods=["PUT"])
@jwt_required()
def update_user(nickname):
    return UserController.update_user(nickname)

@app.route("/api/v1/jwt", methods=["GET"])
@jwt_required()
def protected():
    return UserController.protected()

## PROTECTED 

@app.route("/api/v1/login", methods=["POST"])
def login():
    return UserController.login()

@app.route("/api/v1/user/<nickname>", methods=["GET"])
def get_user(nickname):
    return UserController.get_user(nickname)

@app.route("/api/v1/user", methods=["POST"])
def create_user():
    return UserController.create_user()

@app.route("/", methods=["GET"])
def index():
   return render_template("main.html")


