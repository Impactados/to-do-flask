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
def delete_user(nickname):
    return UserController.delete_user(nickname)

@app.route("/api/v1/user/<nickname>", methods=["PUT"])
def update_user(nickname):
    return UserController.update_user(nickname)

@app.route("/api/v1/jwt", methods=["GET"])
def protected():
    return UserController.protected()

@app.route("/api/v1/task", methods=['POST'])
def create_task():
    return TaskController.create_task()

@app.route("/api/v1/get_task/<user_id>", methods=['GET'])
def get_task(user_id):
    return TaskController.get_task(user_id)

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

# @app.route("/", methods=["GET"])
# def index():
#    return render_template("main.html")

@app.route("/", methods=['GET'])
def render_create_task():
    return render_template('task.html')

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
