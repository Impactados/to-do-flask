from main import app
import controllers

@app.route("/api/v1/user", methods=["POST"])
def create_user():
    return controllers.create_user()

@app.route("/api/v1/login", methods=["POST"])
def login():
    return controllers.login()

if __name__ == '__main__':
    app.run(debug=True, port=5000)