from main import app
import controllers

@app.route("/api/v1/user", methods=["POST"])
def create_user():
    return controllers.create_user()

if __name__ == '__main__':
    app.run(debug=True, port=5000)