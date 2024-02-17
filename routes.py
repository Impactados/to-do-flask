from main import app
import controllers

@app.route("/api/v1/user", methods=["POST"])
def create_user():
    return controllers.create_user()

@app.route("/api/v1/user/<nickname>", methods=["DELETE"])
def delete_user(nickname):
    return controllers.delete_user(nickname)

@app.route("/api/v1/user/<nickname>", methods=["GET"])
def read_user(nickname):
    return controllers.read_user(nickname)

@app.route("/api/v1/user/<nickname>", methods=["PUT"])
def update_user(nickname):
    return controllers.update_user(nickname)

if __name__ == '__main__':
    app.run(debug=True, port=5000)