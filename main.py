import config
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['ALLOW_METHODS_OVERRIDE'] = True
app.config['JWT_SECRET_KEY'] = config.secret
jwt = JWTManager(app)


