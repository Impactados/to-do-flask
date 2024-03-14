import utils
from main import app, jwt
from flask import render_template, jsonify
from flask_jwt_extended import jwt_required
from database.run import execute_sql_file

# controlers
from controllers.user_controller import UserController
from controllers.task_controller import TaskController


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

@app.route("/api/v1/task/<nickname>", methods=['POST'])
@jwt_required()
def create_task(nickname):
    return TaskController.create_task(nickname)

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

# WEB ROUTES

@app.route("/", methods=["GET"])
def index():
   return render_template("main.html")

# CONFIG ROUTES

@app.route('/config/init_db', methods=["GET"])
def init_db():
    success, message = execute_sql_file()
    if success:
        return jsonify({"success": True, "message": message})
    else:
        return jsonify({"success": False, "message": message}), 500


@app.route('/config/connection_db', methods=["GET"])
def test_db_connection():
    conn = utils.connect_database()
    if conn is None:
        return jsonify({"success": False, "message": "Não foi possível estabelecer conexão com o banco de dados."}), 500
    else:
        conn.close()
        return jsonify({"success": True, "message": "Conexão com o banco de dados estabelecida com sucesso."})
