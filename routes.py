import controllers
from main import app, jwt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import jsonify

@app.route("/api/v1/user", methods=["POST"])
def create_user():
    return controllers.create_user()

@app.route("/api/v1/user/<nickname>", methods=["DELETE"])
@jwt_required()
def delete_user(nickname):
    return controllers.delete_user(nickname)

@app.route("/api/v1/user/<nickname>", methods=["GET"])
def get_user(nickname):
    return controllers.get_user(nickname)

@app.route("/api/v1/user/<nickname>", methods=["PUT"])
@jwt_required()
def update_user(nickname):
    return controllers.update_user(nickname)

@app.route("/api/v1/login", methods=["POST"])
def login():
    return controllers.login()

@app.route("/api/v1/jwt", methods=["GET"])
@jwt_required()
def protected():
    return controllers.protected()

if __name__ == '__main__':
    app.run(debug=True, port=5000)