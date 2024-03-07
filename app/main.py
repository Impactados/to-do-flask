from config import Data
from flask import Flask, jsonify, render_template
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['ALLOW_METHODS_OVERRIDE'] = True
app.config['JWT_SECRET_KEY'] = Data.secret
jwt = JWTManager(app)

import routes


if __name__ == '__main__':
    app.run(debug=True, port=5000)