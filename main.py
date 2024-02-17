from flask import Flask, jsonify

app = Flask(__name__)
app.config['ALLOW_METHODS_OVERRIDE'] = True

